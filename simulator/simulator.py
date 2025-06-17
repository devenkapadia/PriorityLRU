from algorithms.priority_lru import PriorityLRUPageReplacement
from algorithms.lru import LRUPageReplacement
from algorithms.fifo import FIFOPageReplacement

class Simulator:
    """Manages simulation of multiple page replacement algorithms."""
    def __init__(self, page_sequence, capacity):
        self.page_sequence = page_sequence
        self.capacity = capacity
        self.algorithms = {
            'PriorityLRU': PriorityLRUPageReplacement(capacity),
            'LRU': LRUPageReplacement(capacity),
            'FIFO': FIFOPageReplacement(capacity)
        }

    def run_all(self):
        """Run all algorithms, return results with detailed logs and priorities."""
        results = {}
        for name, algo in self.algorithms.items():
            faults, log, priorities = algo.run_simulation(self.page_sequence)
            detailed_log = [
                {
                    'time': entry[0],
                    'page': entry[1],
                    'fault': entry[2],
                    'evicted': entry[3] if entry[3] else '-',
                    'cache_state': entry[4]
                } for entry in log
            ]
            results[name] = {'faults': faults, 'log': detailed_log, 'priorities': priorities}
        return results