import random
jackpot = random.randint(1,100)
guess = int(input("Enter the guess"))
counter = 1
while guess != jackpot:
    if guess < jackpot:
        print("Guess Higher")
    else:
        print("Guess Lower")

    guess = int(input("Enter the guess"))
    counter += 1

print("Correct Answer")
print("You took", counter, "attempts")