import random

number = random.randint(0, 100)
chances = 7
print(number)


def game(userAnswer, numbers, chances):
    if userAnswer == numbers:
        print(f'Hurray u got the correct answer {numbers} with chances {chances} left')
        return True
    elif userAnswer > numbers:
        print(f'You are too high u have {chances} left')
        return False
    else:
        print(f'You are too low u have {chances} left')
        return False


while chances > 0:
    print('guess the number')
    guess = int(input('The number is: '))
    chances -= 1
    if game(guess, number, chances):  # Check if the answer is correct
        break  # Exit the loop if the user guesses correctly
    if chances == 0:
        print(f'Sorry, you ran out of chances! The correct number was {number}.')
