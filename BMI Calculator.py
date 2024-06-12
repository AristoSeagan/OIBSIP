def calculate_bmi(weight,height):
    bmi=weight/(height**2)
    return bmi


def bmicategory(bmi):
    if(bmi<18.5):
       return "Underweight"
    elif(bmi>=18.5)and(bmi<24.9):
       return "NormalWeight"
    elif(bmi>=25)and(bmi<29.9):
       return "Overweight"
    else:
       return "Obesity"



height=float(input("Enter the height in meters:"))
weight=float(input("Enter the weight in kilogram:"))

bmi=calculate_bmi(weight,height)
category=bmicategory(bmi)

print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {category}")