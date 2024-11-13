# CS 2520 Team Project
# Performance evaluation of pi computations
# Team members: Pei Yu Kuo, Tiffany Lo, Jesrrel Trujillo, Jonathan Anz

# This is the driver class to test pi computing functions
from PI_Archimedes import Archimedes

import math
import time

def main():

    print()

    # Archimedes method
    print("Archimedes Method:")
    archimedesPI = Archimedes.Calculate_PI(1)
    print("pi =", archimedesPI)
    print("Difference from real pi:", abs(math.pi - archimedesPI))

    # Other methods...

    print()

if __name__ == '__main__':
    main()