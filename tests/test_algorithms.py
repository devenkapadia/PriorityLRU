import pytest
from algorithms.priority_lru import PriorityLRUPageReplacement
from algorithms.lru import LRUPageReplacement
from algorithms.fifo import FIFOPageReplacement

def test_priority_lru():
    algo = PriorityLRUPageReplacement(2)
    sequence = [1, 2, 3, 1]
    faults, _ = algo.run_simulation(sequence)
    assert faults == 3, "Expected 3 faults for PriorityLRU"

def test_lru():
    algo = LRUPageReplacement(2)
    sequence = [1, 2, 3, 1]
    faults, _ = algo.run_simulation(sequence)
    assert faults == 2, "Expected 2 faults for LRU"

def test_fifo():
    algo = FIFOPageReplacement(2)
    sequence = [1, 2, 3, 1]
    faults, _ = algo.run_simulation(sequence)
    assert faults == 3, "Expected 3 faults for FIFO"