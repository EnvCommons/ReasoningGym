# Reasoning-Gym Datasets Catalog

This document catalogs all 105 datasets available in the reasoning-gym package, organized by category.

## Overview

- **Total Datasets**: 105
- **Source**: [reasoning-gym](https://github.com/open-thought/reasoning-gym) Python package
- **All datasets use procedural generation** - no external data required
- **Scoring**: Algorithmic verification via `score_answer()` method (0.0-1.0 reward)
- **Format**: Each task has `{question, answer, metadata}`

---

## 1. ALGEBRA (6 datasets)

### complex_arithmetic
- **Description**: Operations on complex numbers (addition, subtraction, multiplication, division)
- **Sample**: "Calculate (3+4i) * (2-i)"
- **Answer Type**: Complex number string (e.g., "10+5i")

### intermediate_integration
- **Description**: Integration calculus problems of medium difficulty
- **Sample**: "Integrate x^2 * sin(x) dx"
- **Answer Type**: Symbolic expression

### polynomial_equations
- **Description**: Solving polynomial equations
- **Sample**: "Solve: 2x^2 + 5x - 3 = 0"
- **Answer Type**: Solution set (e.g., "x = -3, x = 0.5")

### polynomial_multiplication
- **Description**: Multiplying polynomial expressions
- **Sample**: "Expand: (x+2)(x-3)(x+1)"
- **Answer Type**: Expanded polynomial (e.g., "x^3 - 7x - 6")

### simple_equations
- **Description**: Linear equation solving
- **Sample**: "Solve: 3x + 7 = 22"
- **Answer Type**: Numeric (e.g., "5")

### simple_integration
- **Description**: Basic integration problems
- **Sample**: "Integrate 3x^2 dx"
- **Answer Type**: Symbolic expression (e.g., "x^3 + C")

---

## 2. ALGORITHMIC (34 datasets)

### ab
- **Description**: A::B token rewriting system (inspired by Victor Taelin)
- **Sample**: Apply rewriting rules to transform sequences
- **Answer Type**: Final rewritten sequence

### base_conversion
- **Description**: Converting numbers between different bases (binary, octal, hex, etc.)
- **Sample**: "Convert 255 from base 10 to base 16"
- **Answer Type**: String (e.g., "FF")

### binary_alternation
- **Description**: Pattern detection in binary sequences
- **Sample**: "Does this sequence alternate? 10101010"
- **Answer Type**: Boolean (Yes/No)

### binary_matrix
- **Description**: Matrix manipulation with binary values
- **Sample**: "Transpose this binary matrix: [[1,0],[0,1]]"
- **Answer Type**: Matrix representation

### caesar_cipher
- **Description**: Caesar cipher encryption/decryption
- **Sample**: "Encrypt 'HELLO' with shift 3"
- **Answer Type**: String (e.g., "KHOOR")

### count_primes
- **Description**: Counting prime numbers in ranges
- **Sample**: "How many primes between 1 and 20?"
- **Answer Type**: Integer (e.g., "8")

### cryptarithm
- **Description**: Solving cryptarithmetic puzzles (e.g., SEND+MORE=MONEY)
- **Sample**: "Solve: AB + BA = ACA where each letter is a digit"
- **Answer Type**: Digit mapping (e.g., "A=5, B=4, C=9")

### game_of_life
- **Description**: Conway's Game of Life state computation
- **Sample**: "Compute state after 5 steps"
- **Answer Type**: Grid state

### game_of_life_halting
- **Description**: Predicting Game of Life termination
- **Sample**: "Will this pattern stabilize?"
- **Answer Type**: Boolean + step count

### graph_color
- **Description**: Graph coloring problems
- **Sample**: "Minimum colors needed for this graph?"
- **Answer Type**: Integer + coloring scheme

### group_anagrams
- **Description**: Grouping words into anagram sets
- **Sample**: "Group: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']"
- **Answer Type**: Grouped lists

### isomorphic_strings
- **Description**: Detecting isomorphic strings (pattern matching)
- **Sample**: "Are 'egg' and 'add' isomorphic?"
- **Answer Type**: Boolean

### jugs
- **Description**: Water jug problem solving
- **Sample**: "Fill 4L jug using 5L and 3L jugs"
- **Answer Type**: Sequence of operations

### letter_counting
- **Description**: Counting letter frequencies
- **Sample**: "Count vowels in 'reasoning'"
- **Answer Type**: Integer or frequency dict

### letter_jumble
- **Description**: Unscrambling jumbled letters
- **Sample**: "Unscramble: 'tca'"
- **Answer Type**: String (e.g., "cat")

### manipulate_matrix
- **Description**: Matrix transformation operations
- **Sample**: "Rotate 90° clockwise: [[1,2],[3,4]]"
- **Answer Type**: Transformed matrix

### number_filtering
- **Description**: Filtering numbers by criteria
- **Sample**: "Extract even numbers from [1,2,3,4,5,6]"
- **Answer Type**: List (e.g., "[2,4,6]")

### number_sorting
- **Description**: Sorting numbers with various methods
- **Sample**: "Sort descending: [3,1,4,1,5,9]"
- **Answer Type**: Sorted list

### palindrome_generation
- **Description**: Generating palindromic strings
- **Sample**: "Create a palindrome from 'abc'"
- **Answer Type**: String (e.g., "abcba")

### palindrome_partitioning
- **Description**: Partitioning strings into palindromes
- **Sample**: "Partition 'aab' into palindromes"
- **Answer Type**: Partitions (e.g., "[['a','a','b'],['aa','b']]")

### pool_matrix
- **Description**: Pooling operations on matrices (max/average pooling)
- **Sample**: "Max pool with 2x2 kernel"
- **Answer Type**: Pooled matrix

### ransom_note
- **Description**: Checking if ransom note can be formed from magazine
- **Sample**: "Can 'note' be made from 'stone'?"
- **Answer Type**: Boolean

### rotate_matrix
- **Description**: Rotating matrices by various angles
- **Sample**: "Rotate 180°: [[1,2],[3,4]]"
- **Answer Type**: Rotated matrix

### rotten_oranges
- **Description**: Simulating spread of rot in grid
- **Sample**: "Minutes until all oranges rot?"
- **Answer Type**: Integer

### sentence_reordering
- **Description**: Reordering words to form sentences
- **Sample**: "Reorder: 'is this a test'"
- **Answer Type**: Correct sentence

### spell_backward
- **Description**: Spelling words backward
- **Sample**: "Spell 'hello' backward"
- **Answer Type**: String (e.g., "olleh")

### spiral_matrix
- **Description**: Generating spiral patterns in matrices
- **Sample**: "Create 3x3 spiral from 1-9"
- **Answer Type**: Spiral matrix

### string_insertion
- **Description**: Inserting characters in strings at specific positions
- **Sample**: "Insert 'X' at position 2 in 'hello'"
- **Answer Type**: Modified string

### string_manipulation
- **Description**: Various string operations (reverse, uppercase, etc.)
- **Sample**: "Reverse and uppercase 'test'"
- **Answer Type**: String (e.g., "TSET")

### string_splitting
- **Description**: Splitting strings by patterns
- **Sample**: "Split 'a-b-c' by '-'"
- **Answer Type**: List (e.g., "['a','b','c']")

### string_synthesis
- **Description**: Constructing strings from specifications
- **Sample**: "Create string with 3 'a's and 2 'b's alternating"
- **Answer Type**: String

### word_ladder
- **Description**: Finding transformation paths between words
- **Sample**: "Transform 'cat' to 'dog' changing one letter at a time"
- **Answer Type**: Sequence of words

### word_sequence_reversal
- **Description**: Reversing word sequences
- **Sample**: "Reverse: 'the quick brown fox'"
- **Answer Type**: String (e.g., "fox brown quick the")

### word_sorting
- **Description**: Sorting words by various criteria (alphabetical, length, etc.)
- **Sample**: "Sort alphabetically: ['dog', 'cat', 'bear']"
- **Answer Type**: Sorted list

### gsm_symbolic
- **Description**: Symbolic math from GSM8K dataset (100 embedded tasks)
- **Sample**: Grade school math word problems with symbolic expressions
- **Answer Type**: Numeric answer
- **Note**: Contains 100 sub-tasks

### bf
- **Description**: Brainfuck interpreter/execution
- **Sample**: "Execute Brainfuck program: ++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]"
- **Answer Type**: Program output

### codeio
- **Description**: Code input/output tasks
- **Sample**: Given code and input, predict output
- **Answer Type**: Expected output

---

## 3. ARC (3 datasets)

### arc_1d
- **Description**: 1D Abstraction & Reasoning Corpus tasks (procedural)
- **Sample**: Pattern recognition and transformation in 1D sequences
- **Answer Type**: Transformed sequence
- **Note**: Inspired by François Chollet's ARC challenge

### arc_agi
- **Description**: ARC-AGI variant with transformations
- **Sample**: 2D grid pattern recognition and transformation
- **Answer Type**: Transformed grid

### rearc
- **Description**: Re-engineered ARC tasks
- **Sample**: Abstract reasoning puzzles
- **Answer Type**: Solution grid

---

## 4. ARITHMETIC (18 datasets)

### basic_arithmetic
- **Description**: Basic arithmetic operations (+, -, *, /)
- **Sample**: "Calculate: 15 + 27"
- **Answer Type**: Numeric (e.g., "42")

### bitwise_arithmetic
- **Description**: Bitwise operations (AND, OR, XOR, shift, etc.)
- **Sample**: "Calculate: 5 AND 3"
- **Answer Type**: Integer (e.g., "1")

### calendar_arithmetic
- **Description**: Date and calendar calculations
- **Sample**: "What day is 45 days after Monday, March 1, 2024?"
- **Answer Type**: Day of week

### chain_sum
- **Description**: Chained addition operations
- **Sample**: "Sum: 1 + 2 + 3 + ... + 10"
- **Answer Type**: Integer (e.g., "55")

### count_bits
- **Description**: Counting set bits in numbers
- **Sample**: "How many 1s in binary representation of 7?"
- **Answer Type**: Integer (e.g., "3")

### decimal_arithmetic
- **Description**: Arithmetic with decimal numbers
- **Sample**: "Calculate: 3.5 * 2.25"
- **Answer Type**: Decimal number

### decimal_chain_sum
- **Description**: Chained decimal operations
- **Sample**: "Sum: 1.5 + 2.3 + 0.7"
- **Answer Type**: Decimal number

### dice
- **Description**: Dice rolling and probability calculations
- **Sample**: "Probability of rolling sum of 7 with two dice?"
- **Answer Type**: Fraction or decimal

### fraction_simplification
- **Description**: Reducing fractions to lowest terms
- **Sample**: "Simplify: 12/18"
- **Answer Type**: Fraction (e.g., "2/3")

### gcd
- **Description**: Greatest Common Divisor calculation
- **Sample**: "GCD of 48 and 18?"
- **Answer Type**: Integer (e.g., "6")

### lcm
- **Description**: Least Common Multiple calculation
- **Sample**: "LCM of 12 and 15?"
- **Answer Type**: Integer (e.g., "60")

### leg_counting
- **Description**: Counting total legs from animal lists
- **Sample**: "3 dogs and 2 chickens have how many legs total?"
- **Answer Type**: Integer (e.g., "16")
- **Note**: Quickstart example from reasoning-gym

### number_format
- **Description**: Formatting numbers (significant figures, scientific notation, etc.)
- **Sample**: "Express 0.00045 in scientific notation"
- **Answer Type**: Formatted string

### power_function
- **Description**: Computing powers and exponents
- **Sample**: "Calculate: 2^8"
- **Answer Type**: Integer (e.g., "256")

### prime_factorization
- **Description**: Finding prime factors of numbers
- **Sample**: "Prime factors of 60?"
- **Answer Type**: List (e.g., "[2,2,3,5]")

### products
- **Description**: Computing products of sequences
- **Sample**: "Product: 2 * 3 * 4 * 5"
- **Answer Type**: Integer (e.g., "120")

### time_intervals
- **Description**: Time interval calculations
- **Sample**: "Hours between 9:15 AM and 2:45 PM?"
- **Answer Type**: Duration (e.g., "5.5 hours")

### coin_flip
- **Description**: Probability reasoning with coin flips
- **Sample**: "Probability of 3 heads in 5 flips?"
- **Answer Type**: Probability value

---

## 5. CODE (2 datasets)

### bf
- **Description**: Brainfuck code execution
- **Sample**: Execute Brainfuck programs and predict output
- **Answer Type**: Program output string
- **Note**: Also listed in Algorithmic section

### codeio
- **Description**: Code I/O challenges
- **Sample**: Given code snippet and input, determine output
- **Answer Type**: Expected output
- **Note**: Also listed in Algorithmic section

---

## 6. COGNITION (7 datasets)

### color_cube_rotation
- **Description**: Rotating and visualizing color cubes in 3D
- **Sample**: "After rotating cube left, which color is on top?"
- **Answer Type**: Color name

### figlet_font
- **Description**: ASCII art font rendering
- **Sample**: "Render 'HI' in ASCII art"
- **Answer Type**: Multi-line ASCII art string

### modulo_grid
- **Description**: Grid operations with modulo arithmetic
- **Sample**: Fill grid using modulo patterns
- **Answer Type**: Grid state

### needle_data
- **Description**: Finding needles in haystacks (data retrieval)
- **Sample**: Locate specific data points in large datasets
- **Answer Type**: Data location or value

### needle_haystack
- **Description**: Finding specific data in large text blocks
- **Sample**: "Find the word 'target' in this text"
- **Answer Type**: Position or boolean

### number_sequences
- **Description**: Pattern detection in number sequences
- **Sample**: "Next number: 2, 4, 8, 16, __?"
- **Answer Type**: Integer (e.g., "32")

### rectangle_count
- **Description**: Counting rectangles in grids
- **Sample**: "How many rectangles in a 3x3 grid?"
- **Answer Type**: Integer

---

## 7. GAMES (17 datasets)

### boxnet
- **Description**: Box-drawing puzzle game
- **Sample**: Connect dots to form boxes
- **Answer Type**: Sequence of moves

### countdown
- **Description**: Numbers game from UK game show
- **Sample**: "Use [25, 50, 75, 100, 3, 6] to make 952"
- **Answer Type**: Expression (e.g., "100*10-50+2")
- **Note**: Multiple valid solutions possible

### emoji_mystery
- **Description**: Emoji-based mystery/pattern puzzles
- **Sample**: Decode emoji sequences to find patterns
- **Answer Type**: Solution emoji or pattern

### futoshiki
- **Description**: Japanese inequality grid puzzle
- **Sample**: Fill grid respecting inequality constraints
- **Answer Type**: Completed grid

### kakurasu
- **Description**: Japanese cross-sum puzzle
- **Sample**: Fill grid where sums match constraints
- **Answer Type**: Binary grid solution

### knight_swap
- **Description**: Knight movement puzzle on chessboard
- **Sample**: Swap knight positions with minimum moves
- **Answer Type**: Move sequence

### mahjong_puzzle
- **Description**: Mahjong solitaire
- **Sample**: Remove matching tiles
- **Answer Type**: Sequence of tile pairs

### maze
- **Description**: Maze solving and generation
- **Sample**: "Find path from start to end"
- **Answer Type**: Path coordinates or directions

### mini_sudoku
- **Description**: 4x4 Sudoku variants
- **Sample**: Fill 4x4 grid with 1-4
- **Answer Type**: Completed grid

### n_queens
- **Description**: N-Queens problem solver
- **Sample**: "Place 8 queens on 8x8 board (no attacks)"
- **Answer Type**: Queen positions

### puzzle24
- **Description**: Making 24 from given numbers
- **Sample**: "Use [1,3,4,6] to make 24"
- **Answer Type**: Expression (e.g., "6/(1-3/4)")

### rush_hour
- **Description**: Sliding block puzzle game
- **Sample**: Move blocks to free the target car
- **Answer Type**: Sequence of moves

### sokoban
- **Description**: Warehouse robot puzzle
- **Sample**: Push boxes to target positions
- **Answer Type**: Movement sequence (UDLR)

### sudoku
- **Description**: 9x9 Sudoku puzzle generation and solving
- **Sample**: Fill 9x9 grid with 1-9
- **Answer Type**: Completed grid
- **Note**: Configurable difficulty (17-64 empty cells)

### survo
- **Description**: Finnish logic puzzle
- **Sample**: Fill grid where row/column sums match
- **Answer Type**: Completed grid

### tower_of_hanoi
- **Description**: Tower of Hanoi problem
- **Sample**: "Move 5 disks from A to C"
- **Answer Type**: Sequence of moves (e.g., "A->B, A->C, B->C...")

### tsumego
- **Description**: Go game life-and-death problems
- **Sample**: Determine if stones can be captured/saved
- **Answer Type**: Sequence of moves or outcome
- **Note**: Specialized Go game knowledge required

### rubiks_cube
- **Description**: 3x3, 4x4, 5x5 Rubik's Cube solving
- **Sample**: Solve scrambled cube
- **Answer Type**: Move sequence (e.g., "R U R' U'")
- **Note**: Multiple solutions possible, partial credit supported
- **Special**: `answer` field is `None`, use `metadata['example_correct_answer']`

---

## 8. GEOMETRY (2 datasets)

### simple_geometry
- **Description**: Basic geometric calculations (area, perimeter, angles)
- **Sample**: "Area of triangle with base 5 and height 8?"
- **Answer Type**: Numeric (e.g., "20")

### advanced_geometry
- **Description**: Coordinate geometry (orthocenter, incircle, complex angles)
- **Sample**: "Find circumcenter of triangle with vertices (0,0), (4,0), (2,3)"
- **Answer Type**: Coordinates

---

## 9. GRAPHS (5 datasets)

### course_schedule
- **Description**: Topological sorting for course prerequisites
- **Sample**: "Can you take all courses given these prerequisites?"
- **Answer Type**: Boolean + valid ordering

### family_relationships
- **Description**: Reasoning about family tree relationships
- **Sample**: "If A is B's father and B is C's mother, what is A to C?"
- **Answer Type**: Relationship (e.g., "grandfather")

### largest_island
- **Description**: Finding largest connected components in grids
- **Sample**: Find size of largest island in 2D grid
- **Answer Type**: Integer

### quantum_lock
- **Description**: Graph-based puzzle solving
- **Sample**: Solve quantum lock state puzzle
- **Answer Type**: Solution sequence

### shortest_path
- **Description**: Finding shortest paths in graphs
- **Sample**: "Shortest path from A to E in this graph?"
- **Answer Type**: Path + distance

---

## 10. INDUCTION (2 datasets)

### acre
- **Description**: Blicket causal reasoning experiments
- **Sample**: Determine which objects activate the machine
- **Answer Type**: List of causal objects
- **Note**: Based on cognitive science experiments

### list_functions
- **Description**: Function induction from examples
- **Sample**: "Given f([1,2,3]) = 6 and f([2,3]) = 5, what is f([4,5,6])?"
- **Answer Type**: Numeric

---

## 11. LOGIC (7 datasets)

### aiw
- **Description**: Alice in Wonderland inspired tasks (friends/siblings/colleagues)
- **Sample**: Logic puzzles about relationships
- **Answer Type**: Boolean or entity identification

### circuit_logic
- **Description**: Boolean circuit evaluation
- **Sample**: "Output of AND(OR(A,B), NOT(C)) when A=1, B=0, C=1?"
- **Answer Type**: Boolean (0 or 1)

### knights_knaves
- **Description**: Logic puzzle with truth-tellers and liars
- **Sample**: "A says 'B is a knave.' B says 'We are both knights.' Who is what?"
- **Answer Type**: Entity types (e.g., "A=knight, B=knave")
- **Note**: Flexible scoring accepts multiple answer formats

### propositional_logic
- **Description**: Propositional logic reasoning and truth tables
- **Sample**: "Is (P→Q)∧(Q→R) ⊢ (P→R) valid?"
- **Answer Type**: Boolean + justification

### self_reference
- **Description**: Self-referential logical puzzles
- **Sample**: "This sentence has X words" (solve for X)
- **Answer Type**: Solution value

### syllogism
- **Description**: Classical syllogistic reasoning
- **Sample**: "All A are B. All B are C. Therefore?"
- **Answer Type**: Logical conclusion

### zebra_puzzles
- **Description**: Complex constraint satisfaction puzzles
- **Sample**: "Given clues about houses/colors/pets, who owns the zebra?"
- **Answer Type**: Solution mapping
- **Note**: Complex multi-variable CSP problems

---

## 12. PROBABILITY (1 dataset)

### coin_flip
- **Description**: Probability reasoning with coin flips
- **Sample**: "Probability of exactly 2 heads in 4 fair coin flips?"
- **Answer Type**: Probability (e.g., "0.375" or "3/8")

---

## Special Cases

### Datasets with `answer = None`
- **rubiks_cube**: Use `metadata['example_correct_answer']` instead
- Scoring still works via `score_answer()` method

### Datasets with Multiple Valid Solutions
- **countdown**: Any mathematically correct expression
- **rubiks_cube**: Any valid solution sequence
- **n_queens**: Any valid configuration

### Datasets with Partial Credit
- **rubiks_cube**: Scores 0.05+ for partial progress, 1.0 for complete solution

### Datasets to Skip Initially
- **composite**: Requires special `datasets` parameter for weighted sampling (not a standalone dataset)

---

## Implementation Notes

All datasets:
- Are procedurally generated (deterministic from seed + index)
- Support 500 tasks by default (configurable)
- Use `create_dataset(name, size, seed)` API
- Provide `score_answer(answer, entry)` for verification
- Return entries with `{question, answer, metadata}` structure
- Have curriculum support (101 out of 105 datasets)

## References

- Reasoning-gym GitHub: https://github.com/open-thought/reasoning-gym
- Reasoning-gym GALLERY.md: https://github.com/open-thought/reasoning-gym/blob/main/GALLERY.md
- PyPI package: https://pypi.org/project/reasoning-gym/
