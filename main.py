from simulator.simulator import Simulator
from simulator.workload_generator import WorkloadGenerator
from visualization.plots import plot_comparison, plot_faults_over_time

def main():
    """Run a sample simulation and display results."""
    # Example sequence
    sequence = [1, 2, 3, 4, 1, 5, 6, 7, 1, 8, 9, 10, 1]
    capacity = 3
    
    # Alternative: Generate a workload
    # sequence = WorkloadGenerator.generate_locality(20, 10)
    
    sim = Simulator(sequence, capacity)
    results = sim.run_all()
    
    print("Page Faults:")
    for name, data in results.items():
        print(f"{name}: {data['faults']}")
    
    plot_comparison(results)
    plot_faults_over_time(results)

if __name__ == "__main__":
    main()