import matplotlib.pyplot as plt

def plot_comparison(results):
    """Plot a bar chart comparing page faults across algorithms."""
    labels = list(results.keys())
    faults = [results[name]['faults'] for name in labels]
    
    plt.figure(figsize=(8, 6))
    plt.bar(labels, faults, color=['#4e73df', '#1cc88a', '#e74a3b'])
    plt.title('Page Faults Comparison')
    plt.ylabel('Number of Page Faults')
    plt.xlabel('Algorithm')
    plt.tight_layout()
    plt.show()
    
    # For web: Convert to Chart.js JSON
    # chart_data = {
    #     'type': 'bar',
    #     'data': {
    #         'labels': labels,
    #         'datasets': [{
    #             'label': 'Page Faults',
    #             'data': faults,
    #             'backgroundColor': ['#4e73df', '#1cc88a', '#e74a3b'],
    #             'borderColor': ['#4e73df', '#1cc88a', '#e74a3b'],
    #             'borderWidth': 1
    #         }]
    #     },
    #     'options': {
    #         'scales': {
    #             'y': {'beginAtZero': True, 'title': {'display': True, 'text': 'Number of Page Faults'}}
    #         },
    #         'plugins': {'title': {'display': True, 'text': 'Page Faults Comparison'}}
    #     }
    # }
    # return chart_data

def plot_faults_over_time(results):
    """Plot page faults over time for each algorithm."""
    plt.figure(figsize=(10, 6))
    for name, data in results.items():
        times = [entry[0] for entry in data['log']]
        faults = [sum(1 for entry in data['log'][:i+1] if entry[2]) for i in range(len(data['log']))]
        plt.plot(times, faults, label=name)
    plt.title('Page Faults Over Time')
    plt.xlabel('Time (Access Number)')
    plt.ylabel('Cumulative Page Faults')
    plt.legend()
    plt.tight_layout()
    plt.show()