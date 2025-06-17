from collections import OrderedDict

class LRUPageReplacement:
    """Least Recently Used Page Replacement."""
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.page_faults = 0
        self.log = []  # (time, page, fault, evicted, cache_state)
        self.time = 0
        self.priority = {}  # Dummy for compatibility

    def access_page(self, page):
        """Process a page access, return whether it caused a fault."""
        self.time += 1
        evicted = None
        fault = False

        if page not in self.cache:
            fault = True
            self.page_faults += 1
            if len(self.cache) >= self.capacity:
                evicted, _ = self.cache.popitem(last=False)
            self.cache[page] = True
        else:
            self.cache.move_to_end(page)
        cache_state = list(self.cache.keys())
        self.log.append((self.time, page, fault, evicted, cache_state))
        return fault

    def run_simulation(self, page_sequence):
        """Run simulation on a page sequence, return faults, log, and empty priorities."""
        for page in page_sequence:
            self.access_page(page)
        return self.page_faults, self.log, self.priority