# CS 2520 Team Project
# Performance evaluation of pi computations
# Team members: Pei Yu Kuo, Tiffany Lo, Jesrrel Trujillo, Jonathan Anz

# This is the driver class to test pi computing functions
from PI_Archimedes import Archimedes
from PI_Leibniz import Leibniz
from PI_MonteCarlo import MonteCarlo
from PI_WallisProduct import WallisProduct

import math
import timeit

def main():

    print()

    # Archimedes method
    print("Archimedes Method:")
    archimedes_time = timeit.timeit(lambda: Archimedes.Calculate_PI(50), number=1)
    archimedesPI = Archimedes.Calculate_PI(50)
    print("pi =", archimedesPI)
    print("Difference from real pi:", abs(math.pi - archimedesPI))
    print("Execution time: {:.6f} seconds".format(archimedes_time))

    print()

    # Leibniz method
    print("Leibniz Method:")
    leibniz_time = timeit.timeit(lambda: Leibniz.Calculate_PI(50), number=1)
    leibnizPI = Leibniz.Calculate_PI(50)
    print("pi =", leibnizPI)
    print("Difference from real pi:", abs(math.pi - leibnizPI))
    print("Execution time: {:.6f} seconds".format(leibniz_time))

    print()

    # Monte Carlo method
    print("Monte Carlo Method:")
    montecarlo_time = timeit.timeit(lambda: MonteCarlo.Calculate_PI(50), number=1)
    monteCarloPI = MonteCarlo.Calculate_PI(50)
    print("pi =", monteCarloPI)
    print("Difference from real pi:", abs(math.pi - monteCarloPI))
    print("Execution time: {:.6f} seconds".format(montecarlo_time))

    print()

    # Wallis product method
    print("Wallis product method:")
    wallisproduct_time = timeit.timeit(lambda: WallisProduct.Calculate_PI(50), number=1)
    wallisproductPI = WallisProduct.Calculate_PI(50)
    print("pi =", wallisproductPI)
    print("Difference from real pi:", abs(math.pi - wallisproductPI))
    print("Execution time: {:.6f} seconds".format(wallisproduct_time))

    print()

    # Include more methods?

if __name__ == '__main__':
    main()