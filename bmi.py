username = input('Enter your name: ')
age = int(input('Enter your age: '))
mass = float(input('Enter your mass in kg: '))
height = float(input('Enter your height in meters: '))

bmi = mass / (height ** 2)
print('Hello', username, 'your BMI is:', bmi)