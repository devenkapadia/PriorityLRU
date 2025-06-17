import numpy as np

class WorkloadGenerator:
    """Generates synthetic page sequences for simulation."""
    @staticmethod
    def generate_random(n, page_range):
        """Generate a random sequence of n pages in range [1, page_range]."""
        return np.random.randint(1, page_range + 1, n).tolist()

    @staticmethod
    def generate_locality(n, page_range, hot_pages=3):
        """Generate a sequence with temporal locality."""
        hot = np.random.choice(range(1, page_range + 1), hot_pages, replace=False)
        sequence = []
        for _ in range(n):
            if np.random.random() < 0.8:  # 80% chance for hot page
                sequence.append(np.random.choice(hot))
            else:
                sequence.append(np.random.randint(1, page_range + 1))
        return sequence