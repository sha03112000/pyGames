import random

someWords = '''apple banana mango strawberry
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')

word = random.choice(someWords)

chance = len(word) + 2

print('Game Starts Now')
print('Note: Enter only 1 character at time')

spaces = ["_" for i in range(len(word))]
print(word)
print(spaces)

increment = 0
splitted_words = [x for x in word]
print(splitted_words)

def game():
    guess = input('Enter a letter: ')
    return guess



while chance > 0:

    result = game()
    chance -= 1






