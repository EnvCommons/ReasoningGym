# Reasoning-Gym-Envs

[![OpenReward Environment](https://img.shields.io/badge/%E2%AD%90%20OpenReward-Environment-f7e6cc)](https://openreward.ai/EnvCommons/reasoning-gym-envs)

## Description

Reasoning-Gym-Envs is an environment wrapper for the [reasoning-gym](https://github.com/open-thought/reasoning-gym) Python package, providing 105+ procedurally-generated reasoning datasets as OpenReward environments. It covers 12 categories including algebra, algorithmic problems, ARC variants, arithmetic, code execution, cognition, games, geometry, graphs, induction, logic, and probability.

## Capabilities

- Procedurally-generated reasoning tasks
- Algorithmic answer verification
- Multi-category reasoning evaluation
- Deterministic task generation with seeding

## Compute Requirements

Agents are given a standard environment with no sandbox or file system access.

## License

[Apache 2.0](https://opensource.org/licenses/Apache-2.0).

## Tasks

There is one split per dataset in this environment:

- **train**: 500 tasks per dataset (default, configurable)

Datasets span 12 categories:
- Algebra (6): Complex arithmetic, polynomial equations, integration
- Algorithmic (34): Ciphers, string manipulation, graph problems
- ARC (3): Abstraction & Reasoning Corpus variants
- Arithmetic (18): Basic math, GCD, LCM, prime factorization
- Code (2): Brainfuck execution, code I/O
- Cognition (7): Rubik's cube, pattern recognition, ASCII art
- Games (17): Sudoku, chess puzzles, logic games
- Geometry (2): Basic and advanced geometric calculations
- Graphs (5): Shortest path, topological sort, relationships
- Induction (2): Causal reasoning, function learning
- Logic (7): Knights & Knaves, propositional logic, syllogisms
- Probability (1): Coin flips and probability reasoning

## Reward Structure

This is a single-turn environment. The agent submits an answer via the `submit_answer` tool. Verification is algorithmic via reasoning-gym's `score_answer()` function. Most datasets use exact match scoring (0.0 or 1.0), with some supporting partial credit (e.g., Rubik's cube: 0.0-1.0 based on solution quality).

## Data

No external data files required. All tasks are procedurally generated in-memory using deterministic seeding from the [reasoning-gym package](https://github.com/open-thought/reasoning-gym).

## Tools

| Tool | Description |
|------|-------------|
| `submit_answer` | Submit your answer for algorithmic verification. Ends the episode. |

## Time Horizon

Single-turn. The agent reads the reasoning problem and submits one answer.

## Environment Difficulty

[Put environment difficulty here]

## Other Environment Requirements

None. All evaluation is deterministic and procedurally generated.

## Safety

Agents in Reasoning-Gym-Envs solve reasoning problems in a standard environment. The environment does not present direct safety risks.

## Citation

```bibtex
@misc{stojanovski2025reasoninggymreasoningenvironments,
  title={REASONING GYM: Reasoning Environments for Reinforcement Learning with Verifiable Rewards},
  author={Zafir Stojanovski and Oliver Stanley and Joe Sharratt and Richard Jones and Abdulhakeem Adefioye and Jean Kaddour and Andreas Köpf},
  year={2025},
  eprint={2505.24760},
  archivePrefix={arXiv},
  primaryClass={cs.LG},
  url={https://arxiv.org/abs/2505.24760}
}
```
