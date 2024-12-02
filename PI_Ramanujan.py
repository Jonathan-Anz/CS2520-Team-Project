# This class implements the Ramanujan method for generating pi
import math

class Ramanujan:

    # Function to calculate pi with n iterations (sides)
    # Formula: PI = 1 / ( ( 2*sqrt(2) / 9801 ) * Σ_(k=0)^∞ ( ((4k)! * (1103 + 26390k)) / ((k!)^4 * 396^(4k)) )
    @staticmethod
    def Calculate_PI(n):

        # Initialize the sum term and the PI value as 0
        pi = 0.0 
        sumTerm = 0.0

        # Calculate the factor for the series
        factor = (2 * math.sqrt(2)) / 9801

        # Calculate the sum of the series
        for k in range(n):
            numerator = math.factorial(4 * k) * (1103 + 26390 * k)
            denominator = (math.factorial(k)**4) * (396**(4 * k))
            sumTerm += numerator / denominator

        # Calculate the final PI value
        pi = 1 / (factor * sumTerm)

        return pi
    
    def getName():
        return "Ramanujan"