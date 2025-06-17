import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, request, render_template
from simulator.simulator import Simulator
from simulator.workload_generator import WorkloadGenerator

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/static')

def cumsum(lst):
    """Jinja2 filter for cumulative sum."""
    total = 0
    result = []
    for x in lst:
        total += x
        result.append(total)
    return result

app.jinja_env.filters['cumsum'] = cumsum

@app.route("/", methods=["GET", "POST"])
def index():
    """Handle main page and simulation requests."""
    results = None
    sequence = None
    capacity = 3
    error = None
    if request.method == "POST":
        try:
            sequence_str = request.form.get("sequence", "")
            capacity = int(request.form.get("capacity", 3))
            workload_type = request.form.get("workload_type", "manual")
            
            if workload_type == "random":
                sequence = WorkloadGenerator.generate_random(20, 10)
            elif workload_type == "locality":
                sequence = WorkloadGenerator.generate_locality(20, 10)
            else:
                sequence = [int(x) for x in sequence_str.split() if x.strip()]
            
            if not sequence or capacity < 1:
                raise ValueError("Invalid input: Sequence cannot be empty, and capacity must be positive")
                
            sim = Simulator(sequence, capacity)
            results = sim.run_all()
        except ValueError as e:
            error = str(e)
            
    return render_template("index.html", results=results, sequence=sequence, capacity=capacity, error=error)

if __name__ == "__main__":
    app.run(debug=True, port=8080)