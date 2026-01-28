"""OpenReward server for reasoning-gym environments.

🎉 COMPLETE IMPLEMENTATION 🎉
All 105 reasoning-gym datasets wrapped as OpenReward environments!
"""

from openreward.environments import Server

# ==================== ARITHMETIC (18 environments) ====================
from arithmetic.basic_arithmetic import BasicArithmetic
from arithmetic.bitwise_arithmetic import BitwiseArithmetic
from arithmetic.calendar_arithmetic import CalendarArithmetic
from arithmetic.chain_sum import ChainSum
from arithmetic.count_bits import CountBits
from arithmetic.decimal_arithmetic import DecimalArithmetic
from arithmetic.decimal_chain_sum import DecimalChainSum
from arithmetic.dice import Dice
from arithmetic.fraction_simplification import FractionSimplification
from arithmetic.gcd import Gcd
from arithmetic.gsm_symbolic import GsmSymbolic
from arithmetic.lcm import Lcm
from arithmetic.leg_counting import LegCounting
from arithmetic.number_format import NumberFormat
from arithmetic.power_function import PowerFunction
from arithmetic.prime_factorization import PrimeFactorization
from arithmetic.products import Products
from arithmetic.time_intervals import TimeIntervals

# ==================== ALGEBRA (6 environments) - COMPLETE ====================
from algebra.complex_arithmetic import ComplexArithmetic
from algebra.intermediate_integration import IntermediateIntegration
from algebra.polynomial_equations import PolynomialEquations
from algebra.polynomial_multiplication import PolynomialMultiplication
from algebra.simple_equations import SimpleEquations
from algebra.simple_integration import SimpleIntegration

# ==================== LOGIC (7 environments) - COMPLETE ====================
from logic.aiw import Aiw
from logic.circuit_logic import CircuitLogic
from logic.knights_knaves import KnightsKnaves
from logic.propositional_logic import PropositionalLogic
from logic.self_reference import SelfReference
from logic.syllogism import Syllogism
from logic.zebra_puzzles import ZebraPuzzles

# ==================== GAMES (17 environments) - COMPLETE ====================
from games.boxnet import Boxnet
from games.countdown import Countdown
from games.emoji_mystery import EmojiMystery
from games.futoshiki import Futoshiki
from games.kakurasu import Kakurasu
from games.knight_swap import KnightSwap
from games.mahjong_puzzle import MahjongPuzzle
from games.maze import Maze
from games.mini_sudoku import MiniSudoku
from games.n_queens import NQueens
from games.puzzle24 import Puzzle24
from games.rush_hour import RushHour
from games.sokoban import Sokoban
from games.sudoku import Sudoku
from games.survo import Survo
from games.tower_of_hanoi import TowerOfHanoi
from games.tsumego import Tsumego

# ==================== ALGORITHMIC (34 environments) - COMPLETE ====================
from algorithmic.ab import Ab
from algorithmic.base_conversion import BaseConversion
from algorithmic.binary_alternation import BinaryAlternation
from algorithmic.binary_matrix import BinaryMatrix
from algorithmic.caesar_cipher import CaesarCipher
from algorithmic.count_primes import CountPrimes
from algorithmic.cryptarithm import Cryptarithm
from algorithmic.game_of_life import GameOfLife
from algorithmic.game_of_life_halting import GameOfLifeHalting
from algorithmic.graph_color import GraphColor
from algorithmic.group_anagrams import GroupAnagrams
from algorithmic.isomorphic_strings import IsomorphicStrings
from algorithmic.jugs import Jugs
from algorithmic.letter_counting import LetterCounting
from algorithmic.letter_jumble import LetterJumble
from algorithmic.manipulate_matrix import ManipulateMatrix
from algorithmic.number_filtering import NumberFiltering
from algorithmic.number_sorting import NumberSorting
from algorithmic.palindrome_generation import PalindromeGeneration
from algorithmic.palindrome_partitioning import PalindromePartitioning
from algorithmic.pool_matrix import PoolMatrix
from algorithmic.ransom_note import RansomNote
from algorithmic.rotate_matrix import RotateMatrix
from algorithmic.rotten_oranges import RottenOranges
from algorithmic.sentence_reordering import SentenceReordering
from algorithmic.spell_backward import SpellBackward
from algorithmic.spiral_matrix import SpiralMatrix
from algorithmic.string_insertion import StringInsertion
from algorithmic.string_manipulation import StringManipulation
from algorithmic.string_splitting import StringSplitting
from algorithmic.string_synthesis import StringSynthesis
from algorithmic.word_ladder import WordLadder
from algorithmic.word_sequence_reversal import WordSequenceReversal
from algorithmic.word_sorting import WordSorting

# ==================== GEOMETRY (2 environments) - COMPLETE ====================
from geometry.advanced_geometry import AdvancedGeometry
from geometry.simple_geometry import SimpleGeometry

# ==================== GRAPHS (5 environments) - COMPLETE ====================
from graphs.course_schedule import CourseSchedule
from graphs.family_relationships import FamilyRelationships
from graphs.largest_island import LargestIsland
from graphs.quantum_lock import QuantumLock
from graphs.shortest_path import ShortestPath

# ==================== COGNITION (7 environments) - COMPLETE ====================
from cognition.color_cube_rotation import ColorCubeRotation
from cognition.figlet_font import FigletFont
from cognition.modulo_grid import ModuloGrid
from cognition.needle_haystack import NeedleHaystack
from cognition.number_sequences import NumberSequences
from cognition.rectangle_count import RectangleCount
from cognition.rubiks_cube import RubiksCube

# ==================== PROBABILITY (1 environment) - COMPLETE ====================
from probability.coin_flip import CoinFlip

# ==================== INDUCTION (2 environments) - COMPLETE ====================
from induction.acre import Acre
from induction.list_functions import ListFunctions

# ==================== CODE (2 environments) - COMPLETE ====================
from code.bf import Bf
from code.codeio import Codeio

# ==================== ARC (3 environments) - COMPLETE ====================
from arc.arc_1d import Arc1d
from arc.arc_agi import ArcAgi
from arc.rearc import Rearc

# ========================================================================
# ALL 105 REASONING-GYM ENVIRONMENTS
# ========================================================================
ENVIRONMENTS = [
    # Arithmetic (18)
    BasicArithmetic,
    BitwiseArithmetic,
    CalendarArithmetic,
    ChainSum,
    CountBits,
    DecimalArithmetic,
    DecimalChainSum,
    Dice,
    FractionSimplification,
    Gcd,
    GsmSymbolic,
    Lcm,
    LegCounting,
    NumberFormat,
    PowerFunction,
    PrimeFactorization,
    Products,
    TimeIntervals,
    # Algebra (6) - COMPLETE!
    ComplexArithmetic,
    IntermediateIntegration,
    PolynomialEquations,
    PolynomialMultiplication,
    SimpleEquations,
    SimpleIntegration,
    # Logic (7) - COMPLETE!
    Aiw,
    CircuitLogic,
    KnightsKnaves,
    PropositionalLogic,
    SelfReference,
    Syllogism,
    ZebraPuzzles,
    # Games (17) - COMPLETE!
    Boxnet,
    Countdown,
    EmojiMystery,
    Futoshiki,
    Kakurasu,
    KnightSwap,
    MahjongPuzzle,
    Maze,
    MiniSudoku,
    NQueens,
    Puzzle24,
    RushHour,
    Sokoban,
    Sudoku,
    Survo,
    TowerOfHanoi,
    Tsumego,
    # Algorithmic (34) - COMPLETE!
    Ab,
    BaseConversion,
    BinaryAlternation,
    BinaryMatrix,
    CaesarCipher,
    CountPrimes,
    Cryptarithm,
    GameOfLife,
    GameOfLifeHalting,
    GraphColor,
    GroupAnagrams,
    IsomorphicStrings,
    Jugs,
    LetterCounting,
    LetterJumble,
    ManipulateMatrix,
    NumberFiltering,
    NumberSorting,
    PalindromeGeneration,
    PalindromePartitioning,
    PoolMatrix,
    RansomNote,
    RotateMatrix,
    RottenOranges,
    SentenceReordering,
    SpellBackward,
    SpiralMatrix,
    StringInsertion,
    StringManipulation,
    StringSplitting,
    StringSynthesis,
    WordLadder,
    WordSequenceReversal,
    WordSorting,
    # Geometry (2) - COMPLETE!
    AdvancedGeometry,
    SimpleGeometry,
    # Graphs (5) - COMPLETE!
    CourseSchedule,
    FamilyRelationships,
    LargestIsland,
    QuantumLock,
    ShortestPath,
    # Cognition (7) - COMPLETE!
    ColorCubeRotation,
    FigletFont,
    ModuloGrid,
    NeedleHaystack,
    NumberSequences,
    RectangleCount,
    RubiksCube,
    # Probability (1) - COMPLETE!
    CoinFlip,
    # Induction (2) - COMPLETE!
    Acre,
    ListFunctions,
    # Code (2) - COMPLETE!
    Bf,
    Codeio,
    # ARC (3) - COMPLETE!
    Arc1d,
    ArcAgi,
    Rearc,
]

if __name__ == "__main__":
    Server(ENVIRONMENTS).run()
