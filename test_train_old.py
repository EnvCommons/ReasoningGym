"""Offline tests for the "train_old" split added to every reasoning-gym
wrapper (see base_env.py). No server/network required -- instantiates
wrapper classes directly.

Covers a representative sample of datasets, not all 104 (runtime), including
the two known edge cases found by empirical investigation: calendar_arithmetic
(the worst-case oversample margin) and emoji_mystery (a dataset whose fixed
instruction template itself contains the word "emoji" on every single entry,
so its train_old is legitimately empty -- documented, not a bug).
"""
import pytest

from arithmetic.gcd import Gcd
from arithmetic.calendar_arithmetic import CalendarArithmetic
from arithmetic.gsm_symbolic import GsmSymbolic
from games.sudoku import Sudoku
from games.emoji_mystery import EmojiMystery
from algorithmic.count_primes import CountPrimes
from post2000_filter import mentions_post_2000_topic

SAMPLE_CLASSES = [Gcd, CalendarArithmetic, GsmSymbolic, Sudoku, CountPrimes]


def test_splits_include_train_old():
    for cls in SAMPLE_CLASSES:
        assert cls.list_splits() == ["train", "train_old"]


@pytest.mark.parametrize("cls", SAMPLE_CLASSES)
def test_train_old_has_full_dataset_size(cls):
    tasks = cls.list_tasks("train_old")
    assert len(tasks) == cls.DATASET_SIZE
    assert all(t["split"] == "train_old" for t in tasks)


@pytest.mark.parametrize("cls", SAMPLE_CLASSES)
@pytest.mark.asyncio
async def test_train_old_entries_have_no_post_2000_hits(cls):
    tasks = cls.list_tasks("train_old")
    for t in tasks[:50]:  # sampled, not exhaustive -- full scan is what built the split
        env = cls(task_spec=t)
        prompt = await env.get_prompt()
        text = prompt[0].text
        assert not mentions_post_2000_topic(text), f"{cls.DATASET_NAME} task {t['task_id']} leaks a post-2000 hit"


def test_train_still_full_size_and_unfiltered():
    """train is unaffected by any of this -- same task count as before,
    no filtering applied."""
    for cls in SAMPLE_CLASSES:
        assert len(cls.list_tasks("train")) == cls.DATASET_SIZE


def test_emoji_mystery_train_old_is_empty():
    """Known, expected limitation: every single emoji_mystery entry's fixed
    instruction template contains the literal word "emoji" -- this isn't
    randomly-drawn content oversampling can dodge, it's the dataset's own
    constant framing text. train_old is legitimately empty for this one
    dataset; train is unaffected."""
    assert EmojiMystery.list_tasks("train_old") == []
    assert len(EmojiMystery.list_tasks("train")) == EmojiMystery.DATASET_SIZE


@pytest.mark.asyncio
async def test_train_old_task_resolves_to_a_real_entry():
    env = Gcd(task_spec={"task_id": "0", "split": "train_old"})
    prompt = await env.get_prompt()
    assert prompt[0].text
