import re


def counter(path):
    file = open(path, 'r')

    book_text = file.read()
    file.close()
    book_text = book_text.lower()
    book_text = re.sub("\W|\d", " ", book_text)
    book_text = re.sub("\s+", " ", book_text)
    wordlist = book_text.split(' ')
    diction = {}
    for word in wordlist:
        if diction.get(word) is None:
            diction[word] = 1
        else:
            diction[word] += 1

    return diction

