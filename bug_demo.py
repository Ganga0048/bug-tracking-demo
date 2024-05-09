# bug_demo.py

def divide(a, b):
    return a / b

# Bug: Division by zero possible
result = divide(10, 0)
print("Result:", result)
