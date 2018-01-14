from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as x:
        list1 = []
        for item in x:
          list1.append(item)
        return list1


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score1 = 0
    for characters in word:
        if characters.isalpha():
            score1 += LETTER_SCORES[characters.upper()]
    return score1


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()
    return max(words, key=calc_word_value)


def top_five():
    ls = load_words()
    maxes = list()
    count = 0
    while count < 5:
        maxes.append(max_word_value())
        ls.remove(max_word_value())
        count += 1
    return maxes

if __name__ == "__main__":
    print(load_words())
    print(calc_word_value('Happy'))
    print(max_word_value())
    print(top_five())
