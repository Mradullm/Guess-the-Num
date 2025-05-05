import random as rd

a = rd.randint(1, 100)
while True:
    try:
        b = int(input('Guess the number between 1 and 100: '))
        if a > b:
            print("Your guess was low.")
        elif a < b:
            print("Your guess was high.")
        else:
            print(f"🎉 Your guess is right! The number was {a}.")
            break
    except ValueError:
        print("❌ Invalid input! Please enter an integer.")
