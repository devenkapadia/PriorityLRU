Page Replacement Simulator
A Python-based tool to simulate and visualize page replacement algorithms, including Priority-Based with LRU tie-breaker, LRU, and FIFO).
Installation

Clone the repository:
git clone https://github.com/your_username/page_replacement_simulator.git
cd page_replacement_simulator


Create a virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt



Usage
CLI Mode
Run a sample simulation from the command line:
python main.py

This runs a predefined sequence and displays a bar chart comparing page faults.
Web Interface
Start the web interface:
python visualization/web_interface.py

Open a browser at http://localhost:8080 to input sequences, select workload types, and view results.
Testing
Run unit tests:
pytest tests/

Project Structure

algorithms/: Contains implementations of PriorityLRU, LRU, and FIFO.
simulator/: Manages simulation logic and workload generation.
visualization/: Handles plotting and web interface.
tests/: Unit tests for algorithms and simulator.
test/: Unit tests for algorithms and the simulator.

Features

Simulate three page replacement algorithms.
Generate random or locality-based workloads.
Visualize page faults and faults over time using Matplotlib.
Interactive interface web interface with Flask.
Unit tests for reliability.

Future Improvements

Add more algorithms (e.g., Optimal Page Replacement).
Support real-world memory traces.
Enhance visualizations with Chart.js for web compatibility.
Analyze cache size sensitivity.

License
MIT License
