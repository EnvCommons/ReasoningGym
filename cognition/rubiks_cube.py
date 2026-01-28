"""3x3, 4x4, 5x5 Rubik's Cube solving."""

from base_env import ReasoningGymBase


class RubiksCube(ReasoningGymBase):
    """Rubik's Cube reasoning environment."""

    DATASET_NAME = "rubiks_cube"
