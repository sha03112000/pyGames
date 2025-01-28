import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

chance = 4

print(f'guess any words from this {words}')
while chance > 0:
    user_guess = input('enter your words here: ').lower()
    chance -= 1
    if user_guess == word:
        print(f'brilliant you got it, answer {word}')
        break
    else:
        print(f'oops try again {chance} chances left')
    if chance == 0:
        print(f'correct answer is {word}')