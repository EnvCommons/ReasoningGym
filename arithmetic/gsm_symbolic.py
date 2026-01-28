"""Symbolic math from GSM8K dataset (100 embedded tasks)."""

from base_env import ReasoningGymBase


class GsmSymbolic(ReasoningGymBase):
    """GSM symbolic reasoning environment."""

    DATASET_NAME = "gsm_symbolic"
