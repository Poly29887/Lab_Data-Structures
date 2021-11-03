print(' *** BMI ***')
inp1,inp2 = input('Enter your weight(kg) and height(m) : ').split()
weight = float(inp1)
height = float(inp2)
bmi = weight/(height**2) 
if bmi < 18.5:
    status = 'Below normal weight.'
elif bmi >= 18.5 and bmi < 25:
    status = 'Normal weight.'    
elif bmi >= 25 and bmi < 30:
    status = 'Overweight.'  
elif bmi >= 30 and bmi < 35:
    status = 'Case I Obesity.'  
elif bmi >= 35 and bmi < 40:
    status = 'Case II Obesity.'  
elif bmi >= 40:
    status = 'Case III Obesity.'  
print('Your status is : '+ status)