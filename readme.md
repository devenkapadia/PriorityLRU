# 📄 Page Replacement Simulator

A Python-based simulator to compare and visualize the performance of different page replacement algorithms — including:

- ✅ **PriorityLRU**: A custom algorithm that combines fault-based priority with LRU as a tie-breaker  
- 🔁 **LRU (Least Recently Used)**  
- 🧱 **FIFO (First-In-First-Out)**  

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your_username/page_replacement_simulator.git
cd page_replacement_simulator
```

### 2. Set Up Virtual Environment and Install Dependencies
```bash
python -m venv pagerep
# On Linux/macOS
source pagerep/bin/activate
# On Windows
pagerep\Scripts\activate

pip install -r requirements.txt
```

## Usage

### 1. CLI mode
```bash
python main.py
```

### 2. Web Interface
```bash
python visualization/web_interface.py
```
Then open in browser: http://localhost:8080