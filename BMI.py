print("Please enter your height in meters, using '.' as decimal.")
print()
height = float(input())
print()
print("Please enter your weight in kilograms, using '.' as decimal")
print()
weight = float(input())
print()
BMI = weight // (height*height)

if BMI < 18:
    print("Your BMI is {}".format(BMI), "You are underweight!")
elif BMI < 24:
    print("Your BMI is {}".format(BMI), "Your BMI is healthy!")
else:
    print("Your BMI is {}".format(BMI), "Your are overweight!")

#def BMI(height, weight,):
#    BMI = weight // (height*height)  #(height**2) squared
#    print("Your BMI is {}".format(BMI))
#
#BMI(1.52,63)
