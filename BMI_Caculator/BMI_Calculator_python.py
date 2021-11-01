# create a function to calculate BMI and return the result
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# create a function to calculate the BMI category
def calculate_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# create a function that ask for user's weight and height
def get_weight_and_height():
    weight = float(input("Please enter your weight in kilograms: "))
    height = float(input("Please enter your height in meters: "))
    return weight, height

weight, height = get_weight_and_height()
bmi = calculate_bmi(weight, height)
bmi_category = calculate_bmi_category(bmi)
# print the bmi and the bmi category
print("Your BMI is %.2f and you are %s" % (bmi, bmi_category))


