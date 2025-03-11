import random

def random_number(lower, upper):
    """
    Returns a random number between lower and upper (inclusive).
    
    Args:
        lower (int): The lower bound of the random number range.
        upper (int): The upper bound of the random number range.
    
    Returns:
        int: A random number between lower and upper.
    """
    return random.randint(lower, upper)

# Example usage:
# print(random_number(10, 15))  # Random number between 10 and 15