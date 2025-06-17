import pytest
from simulator.simulator import Simulator

def test_simulator():
    sequence = [1, 2, 3, 4, 1]
    capacity = 2
    sim = Simulator(sequence, capacity)
    results = sim.run_all()
    
    assert 'PriorityLRU' in results
    assert 'LRU' in results
    assert 'FIFO' in results
    assert results['LRU']['faults'] == 3, "Expected 3 faults for LRU"