# CS 2520 Team Project
# Performance evaluation of pi computations
# Team members: Pei Yu Kuo, Tiffany Lo, Jesrrel Trujillo, Jonathan Anz

# This is the driver class to test pi computing functions
from PI_Archimedes import Archimedes
from PI_Leibniz import Leibniz
from PI_MonteCarlo import MonteCarlo

import math
import time

def main():

    print()

    # Archimedes method
    print("Archimedes Method:")
    archimedesPI = Archimedes.Calculate_PI(50)
    print("pi =", archimedesPI)
    print("Difference from real pi:", abs(math.pi - archimedesPI))

    print()

    # Leibniz method
    print("Leibniz Method:")
    leibnizPI = Leibniz.Calculate_PI(50)
    print("pi =", leibnizPI)
    print("Difference from real pi:", abs(math.pi - leibnizPI))

    print()

    # Monte Carlo method
    print("Monte Carlo Method:")
    monteCarloPI = MonteCarlo.Calculate_PI(50)
    print("pi =", monteCarloPI)
    print("Difference from real pi:", abs(math.pi - monteCarloPI))

    print()

    # Include more methods?

if __name__ == '__main__':
    main()