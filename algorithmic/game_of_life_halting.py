"""Predicting Game of Life termination."""

from base_env import ReasoningGymBase


class GameOfLifeHalting(ReasoningGymBase):
    """Game of Life halting reasoning environment."""

    DATASET_NAME = "game_of_life_halting"
