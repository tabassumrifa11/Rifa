print('\033c')

weight = float(input("Enter your weight in KG:"))
height = float(input("Enter your height in meter:"))


bmi = weight / (height*height)

print(f"Your BMI is: {bmi}")


if bmi <= 18.4:
     print("You are under weight")


elif bmi <= 29.9:
     print("You are healthy.")



elif bmi <= 34.9:
     print("You are over weigh.t")



elif bmi <= 39.9:
     print("You are obese.")

else:
     print("You are severly obese.")