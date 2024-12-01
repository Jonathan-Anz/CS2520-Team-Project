# This class implements the wallis product for generating pi

class WallisProduct:

    # Function to calculate pi with n terms
    # Formula: PI = 2 * (∏_(n=1)^∞ ((4n^2) / (4n^2 - 1)))
    @staticmethod
    def Calculate_PI(n):
        # Initialize the sum
        pi = 0.0

        # Initialize the product
        product = 1

        # Loop n number of times    
        for n in range(1, n + 1):
            # Multiplying each terms with the product
            product *= (4 * n**2) / (4 * n**2 - 1)
        
        # Multiply the product by 2 to get π
        pi = product * 2
        
        return pi