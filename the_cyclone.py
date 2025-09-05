height=(input('What is your height in meters? '))
credits=(input('How many credits do you have? '))

if float(height) >= 1.37 and int(credits) >= 10:
    print("Enjoy the ride!")
elif float(height) < 1.37 and  int(credits) >= 10:
    print("You are not tall enough to ride.")
elif float(height) >= 1.37 and int(credits) < 10:
    print("You do not have enough credits.")
else:
    print("You have not met either requirement to ride.")