#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random
from idlelib.multicall import r

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7
hand = []


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    for i in range(NUM_LETTERS):
        rand_choice = random.choice(POUCH)
        hand.append(rand_choice)
    return hand


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    while True:
        word = input("Please suggest a valid word: ").upper()
        try:
            return _validation(word, draw)
        except ValueError as e:
            print(e)
            continue


def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    tempList = list(draw)
    for letters in word.upper():
        if letters in tempList:
            tempList.remove(letters)
        else:
            raise ValueError("Word {} cannot be created from hand!".format(word))
    if not word.lower() in DICTIONARY:
        raise ValueError("{} is not a real word".format(word))
    else:
        return word


# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    valid = []
    for combinations in _get_permutations_draw(draw):
        if combinations.lower() in DICTIONARY:
            valid. append(combinations)
    return valid


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    combo = []
    for i in range(7):
        possible = itertools.permutations(draw, i)
        for x in possible:
            combo.append(''.join(x).lower())
    return combo


# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))
    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    print('\n'.join(_get_permutations_draw(draw)))
    possible_words = get_possible_dict_words(draw)
    print(possible_words)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
