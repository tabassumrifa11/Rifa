print('\033c')

try:

    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))

    result = numerator / denominator

except ZeroDivisionError:
    print("Division by zero is not allowed.")
    
except ValueError:
    print("Invalid input! Please enter a numeric value.")

else:
    print(f"The result is: {result}")

finally:
    print("Execution completed.")