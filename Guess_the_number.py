secret = int("16")

guess = int(input("Guess the number between 1 and 20: "))

if guess == secret:
    print("Congratulate! The number 16 is correct!")
else:
    print("Ouh, you were so close. Try again!")