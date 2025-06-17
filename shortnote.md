# 📄 PriorityLRU Page Replacement – Technical Note

## 🔍 Overview

**PriorityLRU** is a hybrid page replacement algorithm that improves over traditional LRU by adding an additional notion of **priority** based on **historical page fault counts**. It aims to better retain “hot” pages that are accessed frequently over time — even if not recently.

---

## 🔁 Algorithm Logic

1. Each page has an associated **priority**, initialized to `0`.
2. On every **page fault**, increment that page's priority.
3. When a page must be evicted:
   - Evict the page with the **lowest priority**.
   - If multiple pages have the same lowest priority, evict the **Least Recently Used (LRU)** among them.

---

## 📊 Comparison with LRU

| Feature                   | LRU                             | PriorityLRU                                 |
|---------------------------|----------------------------------|---------------------------------------------|
| Eviction Strategy         | Based on recency alone           | Based on fault count, with LRU tie-breaker  |
| Tracks Fault History      | ❌ No                            | ✅ Yes                                       |
| Better for Locality Bias  | ✅ Moderate                      | ✅✅ Strong (retains hot pages longer)       |
| Starvation Possibility    | ❌ No                            | ❌ No (priority eventually grows)           |
| Overhead                  | Low                              | Slightly higher (extra map for priority)    |

> **When is PriorityLRU better than LRU?**  
> In workloads where **some pages are reused frequently but not recently**, LRU might evict them, but PriorityLRU retains them due to their **high fault contribution**.

---

## 💻 Time & Space Complexity

Let:
- `n` = total page references  
- `k` = cache size  

| Operation        | Complexity          |
|------------------|---------------------|
| Lookup           | `O(1)` (via HashSet)|
| Update Recency   | `O(1)` (via deque)  |
| Eviction         | `O(k)` (to find min priority page) |
| Overall per access | `O(k)` worst-case |

> **Note**: With a min-heap or balanced BST by priority, eviction can be improved to `O(log k)`.

---

## 🧪 Example Walkthrough

Let’s simulate the sequence:  

Reference String = [1, 2, 3, 2, 4, 1, 5, 2, 1, 3, 4]
Cache Size = 3

| Step | Page | Cache         | Fault | Priority Map (after access) |
|------|------|---------------|-------|------------------------------|
| 1    | 1    | [1]           | ✅    | {1: 1}                       |
| 2    | 2    | [1, 2]        | ✅    | {1: 1, 2: 1}                 |
| 3    | 3    | [1, 2, 3]     | ✅    | {1: 1, 2: 1, 3: 1}           |
| 4    | 2    | [1, 3, 2]     | ❌    | {1: 1, 2: 1, 3: 1}           |
| 5    | 4    | [3, 2, 4]     | ✅    | {1: 1, 2: 1, 3: 1, 4: 1}     |
| 6    | 1    | [2, 4, 1]     | ✅    | {1: 2, 2: 1, 3: 1, 4: 1}     |
| 7    | 5    | [4, 1, 5]     | ✅    | {1: 2, 2: 1, 3: 1, 4: 1, 5: 1}|
| 8    | 2    | [1, 5, 2]     | ✅    | {1: 2, 2: 2, 3: 1, 4: 1, 5: 1}|
| 9    | 1    | [5, 2, 1]     | ❌    | {1: 2, 2: 2, ...}            |

### 🔸 Observation:

- LRU might evict **frequently used pages** like `1` or `2` early.
- PriorityLRU **retains them** due to their fault count priority.
- Especially useful when workloads revisit old pages periodically.

---

## ✅ Summary

**PriorityLRU** intelligently balances between:
- Keeping frequently faulted pages in cache (for locality)
- Evicting unused or less important ones (like FIFO/LRU)

It may have slightly more overhead than LRU, but often performs **better** in real-world-like workloads with **temporal locality**.

---
