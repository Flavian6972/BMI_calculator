def bmi_calculator():
    height = float(input('What is your height in metres? '))
    weight = float(input('What is your weight in kg? '))
    bmi = weight / (height ** 2)
    print(f' Your BMI is:{bmi}')
    if bmi < 18.5 :
        print('Your are underweight')
    elif 18.5 <= bmi <= 24.9:
        print('Your BMI is normal')
    elif 25 <= bmi <= 29.9:
        print('You are overweight')
    else:
        print('You are obese')


bmi_calculator()



