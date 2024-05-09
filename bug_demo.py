# bug_demo.py

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b

# Bug fixed
result = divide(10, 0)
print("Result:", result)
