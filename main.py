import random

print()

min_val = int(input("Enter the minimum value: "))
max_val = int(input("Enter the maximum value: "))

number = random.randint(min_val, max_val)
guess = int(input(f"\nGuess a number between {min_val} and {max_val}: "))

diff = abs(number - guess)
print(f"\nThe number was {number}. You were off by {diff}.")
