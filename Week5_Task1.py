def charCount(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i, 0) + 1
    return dict


if __name__ == "__main__":
    #input = ['goo', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
    charSet = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
    possible_words(charSet) 
