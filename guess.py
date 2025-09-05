guess = 0
tries = 0

while guess != 6 and tries < 5:
    guess = int(input("Guess the number:  "))
    tries += 1
    if tries == 5 and guess != 6:
        print('You lose!')
        exit()
print("You got it!")

