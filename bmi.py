# 🚨 TharinduRamanayake 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = (int(weight) /float(height**2))

BMI_in_round = round(BMI)
BMI_str = str(BMI_in_round)


if (BMI_in_round < 18.5):
    print ("Your BMI is " + BMI_str + " you are underweight.")
elif (BMI_in_round < 25):
    print ("Your BMI is " + BMI_str + " you have a normal weight.")
elif (BMI_in_round < 30):
    print ("Your BMI is " + BMI_str + " you are slightly overweight.")
elif (BMI_in_round < 35):
    print ("Your BMI is " + BMI_str + " you are obese.")
else:
    print ("Your BMI is " + BMI_str + " you are clinically obese.")

