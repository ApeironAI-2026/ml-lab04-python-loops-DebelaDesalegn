def calculate_factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    Example: 5! = 120
    """
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    
    # 1. Initialize result
    result = 1

    # 2. Loop from 1 to n and multiply
    for i in range(1, n + 1):
        result *= i

    # 3. Return the result
    return result