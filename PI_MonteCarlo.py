# This class implements the monte carlo method for generating pi
import random

class MonteCarlo:

    # Function to calculate pi with n points
    # Formula: PI = 4 * (points_inside_circle / total_points)
    @staticmethod
    def Calculate_PI(n):

        # Count points within circle
        inside_count = 0

        # Loop n number of times
        for _ in range(n):
            # Generate random (x, y) point in the square [0, 1] x [0, 1]
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)

            # Check if the point lies inside the quarter-circle
            if x ** 2 + y ** 2 <= 1:
                inside_count += 1

        # Estimate PI with the formula
        return 4 * (inside_count / n)