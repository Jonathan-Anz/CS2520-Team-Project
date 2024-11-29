# This class implements the leibniz formula for generating pi

class Leibniz:

    # Function to calculate pi with n terms
    # Formula: PI = 4 * Σ [((-1)^k) / (2k + 1)], for k = 0 to n-1
    @staticmethod
    def Calculate_PI(n):
        # Initialize the sum
        pi = 0.0
        # Loop n number of times
        for k in range(n):
            # Add the k-th term
            pi += ((-1)**k) / (2 * k + 1)
        # Multiply by 4 to get π
        return 4 * pi