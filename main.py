x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))

operation = input("Choose math operation (+, -, *, /: ")

if operation == "+":
    print(x+y)
elif operation == "-":
    print(x-y)
elif operation == "*":
    print(x*y)
elif operation == "/":
    print(x/y)
else:
    print("Error.")