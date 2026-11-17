# Lab Exercise 5: Number guessing game
number = 7

guess = int(input("Guess the number: "))

if guess == number:
    print("Correct guess")
elif guess > number:
    print("Too high")
else:
    print("Too low")
