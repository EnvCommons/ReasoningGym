"""Base environment class for all reasoning-gym dataset wrappers.

This module provides a shared base class that handles all common logic
for wrapping reasoning-gym datasets as OpenReward environments.
"""

from __future__ import annotations

from typing import ClassVar

import reasoning_gym
from openreward.environments import Environment, JSONObject, TextBlock, ToolOutput, tool
from pydantic import BaseModel, Field

from post2000_filter import mentions_post_2000_topic


class SubmitAnswerInput(BaseModel):
    """Input schema for the submit_answer tool."""

    answer: str = Field(..., description="Your answer to the question")


class ReasoningGymBase(Environment):
    """Base class for all reasoning-gym dataset wrappers.

    This class provides all the common functionality needed to wrap a
    reasoning-gym dataset as an OpenReward environment. Individual dataset
    wrappers only need to set the DATASET_NAME class variable.

    Attributes:
        DATASET_NAME: Name of the reasoning-gym dataset (must be set by subclass)
        DATASET_SIZE: Number of tasks to generate (default: 500)
        DATASET_SEED: Random seed for reproducibility (default: 42)
    """

    # Subclasses must override these class variables
    DATASET_NAME: ClassVar[str] = None
    DATASET_SIZE: ClassVar[int] = 1000
    DATASET_SEED: ClassVar[int] = 42

    # "train_old" oversamples this many multiples of DATASET_SIZE (same seed,
    # so entries 0..DATASET_SIZE-1 are identical to "train"'s -- reasoning_gym
    # generation is deterministic and index-stable across different `size`
    # values for the same seed), then keeps the first DATASET_SIZE entries
    # whose question text has no post-2000 hit. A handful of datasets embed a
    # random real-world year/date or draw from a template pool that includes
    # a few modern-sounding words; oversampling absorbs that without special-
    # casing every dataset individually.
    OLD_OVERSAMPLE: ClassVar[int] = 8

    @classmethod
    def list_splits(cls) -> list[str]:
        """Return available data splits."""
        return ["train", "train_old"]

    @classmethod
    def _old_filtered_indices(cls) -> list[int]:
        """Indices into the oversampled dataset whose question passes the
        filter, capped at DATASET_SIZE. Cached per class."""
        if not hasattr(cls, "_old_filtered_indices_cache"):
            oversampled = reasoning_gym.create_dataset(
                cls.DATASET_NAME, size=cls.DATASET_SIZE * cls.OLD_OVERSAMPLE, seed=cls.DATASET_SEED
            )
            indices = []
            for i in range(len(oversampled)):
                if not mentions_post_2000_topic(oversampled[i]["question"]):
                    indices.append(i)
                    if len(indices) >= cls.DATASET_SIZE:
                        break
            cls._old_dataset_cache = oversampled
            cls._old_filtered_indices_cache = indices
        return cls._old_filtered_indices_cache

    @classmethod
    def list_tasks(cls, split: str) -> list[JSONObject]:
        """List all available tasks for a given split.

        Args:
            split: The data split ("train" or "train_old")

        Returns:
            List of task specifications with task_id (and split, for "train_old")
        """
        if split == "train":
            return [{"task_id": str(i)} for i in range(cls.DATASET_SIZE)]
        if split == "train_old":
            n = len(cls._old_filtered_indices())
            return [{"task_id": str(i), "split": "train_old"} for i in range(n)]
        return []

    def __init__(self, task_spec: JSONObject, secrets: dict[str, str] = {}) -> None:
        """Initialize the environment with a specific task.

        Args:
            task_spec: Task specification containing task_id (and optionally
                split="train_old" -- absent/"train" behaves as before)
            secrets: API keys and secrets (not used for reasoning-gym)
        """
        super().__init__(task_spec)

        split = task_spec.get("split", "train")
        self.task_id = int(task_spec["task_id"])

        if split == "train_old":
            filtered_indices = self.__class__._old_filtered_indices()
            self.dataset = self.__class__._old_dataset_cache
            self.entry = self.dataset[filtered_indices[self.task_id]]
        else:
            # Class-level dataset caching: create dataset once per class, not per task
            # This significantly improves performance when multiple tasks are run
            if not hasattr(self.__class__, "_dataset_cache"):
                self.__class__._dataset_cache = reasoning_gym.create_dataset(
                    self.DATASET_NAME, size=self.DATASET_SIZE, seed=self.DATASET_SEED
                )
            self.dataset = self.__class__._dataset_cache
            self.entry = self.dataset[self.task_id]

    async def get_prompt(self) -> list[TextBlock]:
        """Get the prompt/question for this task.

        Returns:
            List containing a single TextBlock with the question and tool instruction
        """
        prompt_text = self.entry["question"] + "\n\nSubmit your answer using the submit_answer tool."
        return [TextBlock(text=prompt_text)]

    @tool
    async def submit_answer(self, params: SubmitAnswerInput) -> ToolOutput:
        """Submit your answer for algorithmic verification.

        This tool uses the reasoning-gym package's built-in scoring mechanism
        to verify the answer. Scores range from 0.0 (incorrect) to 1.0 (correct),
        with some datasets supporting partial credit.

        Args:
            params: Input containing the answer string

        Returns:
            ToolOutput with feedback, score, and metadata
        """
        # Use reasoning-gym's algorithmic verification
        score = self.dataset.score_answer(answer=params.answer, entry=self.entry)

        # Determine feedback message based on score
        if score == 1.0:
            feedback = "✅ Correct!"
        elif score > 0.0:
            feedback = f"⚠️ Partially correct (score: {score:.2f})"
        else:
            feedback = "❌ Incorrect"

        # Include expected answer if available and answer is incorrect
        expected = self.entry.get("answer")
        if expected is not None and score < 1.0:
            feedback += f"\n\nExpected answer: {expected}"

        # Build metadata for debugging and analysis
        metadata = {
            "task_id": self.task_id,
            "dataset": self.DATASET_NAME,
            "submitted_answer": params.answer,
            "expected_answer": expected,
            "score": score,
        }

        # Include example correct answer if provided in metadata (e.g., rubiks_cube)
        if "example_correct_answer" in self.entry.get("metadata", {}):
            example_answer = self.entry["metadata"]["example_correct_answer"]
            metadata["example_correct_answer"] = example_answer
            if score < 1.0:
                feedback += f"\n\nExample correct answer: {example_answer}"

        return ToolOutput(
            blocks=[TextBlock(text=feedback)],
            metadata=metadata,
            reward=score,
            finished=True,
        )
