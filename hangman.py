from random import choice
from termcolor import colored
import json

with open('/randword.json') as f:
    import_json = json.loads(f.read())
words = import_json['data']


def hint(s1):
    return ''.join(['-' if letter not in guessed_letters else letter for letter in s1])


word = choice(words)
guessed_letters = set()

print(colored('H A N G M A N', 'red'))
opt_in = input('Type "play" to play, or "exit" to quit: ')

turns = 0
while turns < 8 and opt_in == 'play':
    print()
    print(hint(word))
    guess = input('Input a letter: ')

    if len(guess) != 1:
        print('You should input a single letter')
    elif not guess.isascii() or not guess.islower():
        print('It is not an ASCII lowercase letter')
    elif guess in guessed_letters:
        print('You already typed this letter')
    elif guess not in word:
        print('No such letter in the word')
        guessed_letters.add(guess)
        turns += 1
    else:
        guessed_letters.add(guess)

    if hint(word) == word:
        print()
        print(f'Word was {word}')
        print('You survived!')
        print()
        opt_in = input('Type "play" to play, or "exit" to quit: ')
        if opt_in == 'play':
            word = choice(words)
            turns = 0
            guessed_letters = set()
        else:
            print()
            print('Thanks for playing!')
            break

    if turns == 8:
        print()
        print(f'Word was {word}')
        print('You are hanged!')
        print()
        opt_in = input('Type "play" to play, or "exit" to quit: ')
        if opt_in == 'play':
            word = choice(words)
            turns = 0
            guessed_letters = set()
        else:
            print()
            print('Thanks for playing!')
            break
