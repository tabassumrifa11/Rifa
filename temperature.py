print('\033c')

tem = input("Enter the temperature in Celsius: ")
tem = int(tem)

fer = (9/5) * tem + 32
print(f"Fahrenheit:{fer}")


kel = tem + 273.15
print(f"Kelvin:{kel}")


rn = (9/5) * tem + 492
print(f"Rankine:{rn}")

r = (4/5) * tem
print(f"Reaumur:{r}")
