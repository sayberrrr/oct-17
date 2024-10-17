def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


choice = input("Enter choice (1/2/3/4): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


if choice in ['1', '2', '3', '4']:
    operations = [add, subtract, multiply, divide]
    selected_operation = operations[int(choice) - 1]
    
    result = selected_operation(num1, num2)
    print("Result: ", result)
else:
    print("Invalid input")