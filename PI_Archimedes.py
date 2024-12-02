# This class implements the archimedes approach for generating pi
import math

class Archimedes:

    # Function to calculate pi with n iterations (sides)
    # Formula: PI = sin(360 / 2n) * n
    @staticmethod
    def Calculate_PI(n):

        try:
            value = 360 / (n * 2)
            sinValue = math.sin(math.radians(value))
            pi = sinValue * n

            return pi
        
        except ZeroDivisionError:
            print("n cannot be zero!")
            return 0
        
    def getName():
        return "Archimedes"