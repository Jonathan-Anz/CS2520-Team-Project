# %%
import matplotlib.pylab as plt

# Define a class to generate the graph using the matplotlib library
class Graph():
    
    # List of methods to be evaluated
    methods = ["Archimedes", "Leibniz", "Monte Carlo", "Wallis Product", "Ramanujan"]
    # List to store the number of iterations for each method
    iterations = []
    # List to store the execution times for each method
    executionTimes = {}
    # List to store the difference between calculated pi and the real pi for each method
    PIDifference = {}
    
    # Constructor to initialize the graph with execution times and iterations
    def __init__(self, executionTime, iterations, difference):
        self.executionTimes = executionTime.copy()
        self.iterations = iterations
        self.PIDifference = difference.copy()
   
    # Method to generate the graph
    def getExecutionTimeGraph(self):
        # Creating a new figure with a specified size
        plt.figure(figsize=(12, 8))

        # Plotting the execution time against the number of iterations for each method
        for method in self.methods:
            plt.plot(self.iterations, self.executionTimes[method], marker='o', label=method)

        # Setting the plot parameters
        plt.xlabel('Iterations')
        plt.ylabel('Execution Time (seconds)')
        plt.title('Execution Time vs Iterations for Different Methods')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    # Method to generate the graph
    def getPIDifferenceGraph(self):
        # Creating a new figure with a specified size
        plt.figure(figsize=(12, 8))

        # Plotting the pi difference against the number of iterations for each method
        for method in self.methods:
            plt.plot(self.iterations, self.PIDifference[method], marker='o', label=method)

        # Setting the plot parameters
        plt.xlabel('Iterations')
        plt.ylabel('Difference from real pi')
        plt.title('Difference from real pi vs Iterations for Different Methods')
        plt.legend()
        plt.grid(True)
        plt.show()