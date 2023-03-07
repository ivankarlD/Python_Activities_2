number = int(input("Enter an integer: "))
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1
print("Factorial is:", factorial)
