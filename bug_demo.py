# bug_demo.py

def divide(a, b):
    """
    Divide two numbers.

    :param a: The numerator.
    :type a: float or int
    :param b: The denominator.
    :type b: float or int
    :return: The result of the division. If division by zero occurs, returns an error message.
    :rtype: float or str
    """
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b

# Bug fixed
result = divide(10, 0)
print("Result:", result)
