# CS 2520 Team Project
# Performance evaluation of pi computations
# Team members: Pei Yu Kuo, Tiffany Lo, Jesrrel Trujillo, Jonathan Anz

# This is the driver class to test pi computing functions
from PI_Archimedes import Archimedes
from PI_Leibniz import Leibniz
from PI_MonteCarlo import MonteCarlo
from PI_WallisProduct import WallisProduct
from PI_Ramanujan import Ramanujan

import math
import timeit

# List to store the test results of each method
results = []

# Function to test pi computation methods
def runPITest(method, iterations):
    print()

    print(method.getName() + " Method:\n")

    # Methods to be tested
    for iter in iterations:
        method_time = timeit.timeit(lambda: method.Calculate_PI(iter), number=1)
        methodPI = method.Calculate_PI(iter)
        results.append([method.getName(), methodPI, abs(math.pi - methodPI), iter, method_time])
        print("pi =", methodPI)
        print("Difference from real pi:", abs(math.pi - methodPI))
        print("Iterations preformed: ", iter)
        print("Execution time: {:.6f} seconds".format(method_time))
        print()

    print(100 * "*", "\n")

# print the test results of each method in a table format
def printResultsTable(result):
    print('The results table of the test for each method:\n')
    print('{:^15s} | {:^20s} | {:^25s} | {:^15s} | {:^25s}'.format('Method', 'pi', 'Difference', 'Iterations', 'Execution Time'))
    print('-' * (15+20+25+15+15+20))
    for result in results:
        print('{:^15s} | {:^20.15f} | {:^25.15f} | {:^15d} | {:^25.15f}'.format(result[0], result[1], result[2], result[3], result[4]))
        print('-' * (15+20+25+15+15+20))

def main():
    # For Ramanujan method, iterations greater than 1000 will 
    # cause the execution time to be at least 0.5 seconds

    # List of iterations to run
    NUM_ITERATIONS = [50, 500, 1000, 2000, 3000]

    # List of methods to test
    methods = [Archimedes, Leibniz, MonteCarlo, WallisProduct, Ramanujan]
    
    # Run pi computation tests and print the results for each method 
    for method in methods:
        runPITest(method, NUM_ITERATIONS)
    
    # Print the results table
    printResultsTable(results)
    
if __name__ == '__main__':
    main()