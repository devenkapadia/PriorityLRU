from collections import defaultdict

class PriorityLRUPageReplacement:
    """Priority-Based Page Replacement with LRU tie-breaker."""
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = set()
        self.priority = defaultdict(int)  # page -> #faults caused
        self.last_used = dict()  # page -> last access time
        self.time = 0
        self.page_faults = 0
        self.log = []  # (time, page, fault, evicted, cache_state)

    def access_page(self, page):
        """Process a page access, return whether it caused a fault."""
        self.time += 1
        evicted = None
        fault = False

        if page not in self.cache:
            fault = True
            self.page_faults += 1
            self.priority[page] += 1
            if len(self.cache) >= self.capacity:
                min_priority = min(self.priority[p] for p in self.cache)
                candidates = [p for p in self.cache if self.priority[p] == min_priority]
                evicted = min(candidates, key=lambda p: self.last_used[p])
                self.cache.remove(evicted)
            self.cache.add(page)
        self.last_used[page] = self.time
        cache_state = sorted(list(self.cache))
        self.log.append((self.time, page, fault, evicted, cache_state))
        return fault

    def run_simulation(self, page_sequence):
        """Run simulation on a page sequence, return faults, log, and priorities."""
        for page in page_sequence:
            self.access_page(page)
        return self.page_faults, self.log, dict(self.priority)