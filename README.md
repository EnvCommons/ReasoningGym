# Reasoning-Gym OpenReward Environments

OpenReward environment wrappers for the [reasoning-gym](https://github.com/open-thought/reasoning-gym) Python package. This repository provides 105+ procedurally-generated reasoning datasets as OpenReward environments, ready for agent training and evaluation.

## Overview

The reasoning-gym package provides diverse reasoning tasks across 12 categories:
- **Algebra** (6 datasets): Complex arithmetic, polynomial equations, integration
- **Algorithmic** (34 datasets): Ciphers, string manipulation, graph problems
- **ARC** (3 datasets): Abstraction & Reasoning Corpus variants
- **Arithmetic** (18 datasets): Basic math, GCD, LCM, prime factorization
- **Code** (2 datasets): Brainfuck execution, code I/O
- **Cognition** (7 datasets): Rubik's cube, pattern recognition, ASCII art
- **Games** (17 datasets): Sudoku, chess puzzles, logic games
- **Geometry** (2 datasets): Basic and advanced geometric calculations
- **Graphs** (5 datasets): Shortest path, topological sort, relationships
- **Induction** (2 datasets): Causal reasoning, function learning
- **Logic** (7 datasets): Knights & Knaves, propositional logic, syllogisms
- **Probability** (1 dataset): Coin flips and probability reasoning

See [DATASETS.md](DATASETS.md) for the complete catalog of all 105 datasets.

## Features

- **105 Reasoning Datasets** wrapped as OpenReward environments
- **Procedurally Generated**: Unlimited tasks with deterministic seeding
- **Algorithmic Verification**: Automatic scoring via reasoning-gym
- **No External Data**: All datasets generated in-memory
- **Simple Architecture**: One base class handles all 105 datasets
- **4-Line Wrappers**: Each dataset wrapper is only 4 lines of code

## Architecture

### Core Design

The repository uses a **monorepo with shared base class** approach:

1. **`base_env.py`** - Contains all common logic (200 lines)
   - Task listing and prompt generation
   - Submit answer tool with algorithmic verification
   - Class-level dataset caching for performance

2. **Individual Dataset Wrappers** - Only 4 lines each!
   ```python
   from base_env import ReasoningGymBase

   class BasicArithmetic(ReasoningGymBase):
       DATASET_NAME = "basic_arithmetic"
   ```

3. **`server.py`** - Registers all environments with OpenReward

### Why This Works

- All reasoning-gym datasets follow identical patterns
- `create_dataset(name, size, seed)` → uniform dataset interface
- `score_answer(answer, entry)` → uniform scoring (0.0-1.0)
- Each entry has `{question, answer, metadata}` structure

## Quick Start

### Prerequisites

- Python >= 3.10
- OpenReward SDK
- reasoning-gym package

### Installation

```bash
# Clone the repository
git clone https://github.com/EnvCommons/reasoning-gym-envs.git
cd reasoning-gym-envs

# Install dependencies
pip install -r requirements.txt
```

### Running the Server Locally

```bash
# Start the OpenReward environment server
python server.py
```

The server will start on `http://0.0.0.0:8080` and expose:
- `BasicArithmetic` environment
- `KnightsKnaves` environment

### Testing with an Agent

```bash
# Set your OpenAI API key
export OPENAI_API_KEY="your-key-here"

# Run the test agent
python test_agent.py
```

Example output:
```
================================================================================
Testing environment: local/BasicArithmetic
Total tasks available: 500
================================================================================

Testing task 0: {'task_id': '0'}

Question: Calculate: 15 + 27

Model called tool: submit_answer
Arguments: {"answer": "42"}

────────────────────────────────────────────────────────────────────────────────
Tool result:
  Reward: 1.000
  Finished: True
  Feedback: ✅ Correct!
────────────────────────────────────────────────────────────────────────────────
```

## Project Structure

```
reasoning-gym-envs/
├── README.md                      # This file
├── DATASETS.md                    # Complete catalog of 105 datasets
├── base_env.py                    # Shared base class (all logic here)
├── server.py                      # Server registration
├── test_agent.py                  # Testing harness
├── requirements.txt               # Dependencies
├── Dockerfile                     # Docker deployment
├── arithmetic/
│   ├── __init__.py
│   └── basic_arithmetic.py        # Example: 4-line wrapper
└── logic/
    ├── __init__.py
    └── knights_knaves.py          # Example: 4-line wrapper
```

## Usage Examples

### Basic Arithmetic

```python
# Task example
Question: "Calculate: 15 + 27"
Answer: "42"
Reward: 1.0
```

### Knights and Knaves

```python
# Task example
Question: "A says 'B is a knave.' B says 'We are both knights.' Who is what?"
Answer: "A=knight, B=knave"
Reward: 1.0
```

## Docker Deployment

### Build Image

```bash
docker build -t reasoning-gym-envs:latest .
```

### Run Container

```bash
docker run -p 8080:8080 reasoning-gym-envs:latest
```

### Test Dockerized Server

```bash
export OPENAI_API_KEY="your-key-here"
python test_agent.py
```

## Adding New Datasets

To add more reasoning-gym datasets (currently showing 2 of 105):

### Option 1: Manual Addition

1. Create a new category directory (if needed):
   ```bash
   mkdir -p geometry
   touch geometry/__init__.py
   ```

2. Create the wrapper file (4 lines):
   ```python
   # geometry/simple_geometry.py
   from base_env import ReasoningGymBase

   class SimpleGeometry(ReasoningGymBase):
       DATASET_NAME = "simple_geometry"
   ```

3. Update `server.py`:
   ```python
   from geometry.simple_geometry import SimpleGeometry

   Server([BasicArithmetic, KnightsKnaves, SimpleGeometry]).run()
   ```

### Option 2: Automated Generation

Use the `generate_envs.py` script (coming soon) to auto-generate all 103 remaining wrappers:

```bash
python generate_envs.py
```

This will:
- Create all 12 category directories
- Generate 103 4-line wrapper files
- Update `server.py` with all imports

## Configuration

### Dataset Size

Change the number of tasks per dataset (default: 500):

```python
class BasicArithmetic(ReasoningGymBase):
    DATASET_NAME = "basic_arithmetic"
    DATASET_SIZE = 1000  # Generate 1000 tasks instead of 500
```

### Random Seed

Change the random seed for reproducibility (default: 42):

```python
class BasicArithmetic(ReasoningGymBase):
    DATASET_NAME = "basic_arithmetic"
    DATASET_SEED = 123  # Use different seed
```

## Testing

### Syntax Check

```bash
python -m py_compile base_env.py arithmetic/basic_arithmetic.py logic/knights_knaves.py
```

### Local Server Test

```bash
# Terminal 1: Start server
python server.py

# Terminal 2: Test with agent
export OPENAI_API_KEY="your-key-here"
python test_agent.py
```

### Docker Test

```bash
docker build -t reasoning-gym-envs:test .
docker run -p 8080:8080 reasoning-gym-envs:test
python test_agent.py
```

## Environment Details

### Tools Provided

Each environment exposes one tool:

- **`submit_answer(answer: str)`**
  - Submit your answer for algorithmic verification
  - Returns reward (0.0-1.0) and feedback
  - Supports partial credit for some datasets (e.g., Rubik's cube)

### Splits Available

- **`train`** - All reasoning-gym datasets are training data (500 tasks each by default)

### Task Format

Each task includes:
```python
{
    "question": "Calculate: 15 + 27",
    "answer": "42",
    "metadata": {
        "source_dataset": "basic_arithmetic",
        "source_index": 0,
        ...
    }
}
```

### Scoring

- **Exact Match**: Most datasets (0.0 or 1.0)
- **Partial Credit**: Some datasets like Rubik's cube (0.0-1.0)
- **Multiple Solutions**: Some datasets accept multiple valid answers (countdown, n_queens)

## Special Cases

### Datasets with `answer = None`

- **rubiks_cube**: Answer field is `None`, but scoring still works via `score_answer()`
- The base class automatically handles this and shows `example_correct_answer` from metadata

### Datasets with Multiple Valid Solutions

- **countdown**: Any mathematically correct expression
- **rubiks_cube**: Any valid solution sequence
- **n_queens**: Any valid queen placement

The reasoning-gym scoring handles all these cases automatically.

## Performance Notes

- **Class-level caching**: Datasets are created once per class, not per task
- **Lazy loading**: Tasks are generated on-demand from seed + index
- **Memory efficient**: No external data files or large memory footprint
- **Fast startup**: Server starts in seconds

## Contributing

To add more datasets:

1. Check [DATASETS.md](DATASETS.md) for available datasets
2. Create a 4-line wrapper in the appropriate category folder
3. Update `server.py` to register the new environment
4. Test with `python test_agent.py`
5. Submit a pull request

## Resources

- **Reasoning-gym GitHub**: https://github.com/open-thought/reasoning-gym
- **Reasoning-gym GALLERY**: https://github.com/open-thought/reasoning-gym/blob/main/GALLERY.md
- **OpenReward Docs**: https://docs.openreward.org/
- **Dataset Catalog**: [DATASETS.md](DATASETS.md)

## License

This project follows the same license as the reasoning-gym package (Apache 2.0).

## Acknowledgments

- **reasoning-gym**: For providing 105 high-quality reasoning datasets
- **OpenReward**: For the environment framework
- **open-thought**: For creating and maintaining reasoning-gym
