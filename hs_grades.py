# #U.S. high schools typically last for four years, from freshman year to senior year. 🚌💨
# #First, ask the user to enter their grade as an integer.
# Create a four-year high school grade system using an if/elif/else statement:
# grade is 9, print 'Freshman'
# grade is 10, print 'Sophomore'
# grade is 11, print 'Junior'
# grade is 12, print 'Senior'
# Everything else is 'TBD'

grade = int(input('Enter your High School Grade (9-12): '))

if grade >= 9 and grade <= 12:
    if grade == 9:
        print('Freshman')
    elif grade == 10:
        print('Sophomore')
    elif grade == 11:
        print('Junior')
    elif grade == 12:
        print('Senior')
    else:
        print('TBD')
else:
    print("Invalid grade. Please enter a number between 9 and 12.")