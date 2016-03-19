import re


def counter(path):
    file = open(path, 'rt')
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

    for elem in diction:
        diction[elem] = (100 * diction[elem]) / wordlist.__len__()

    return diction


def table_maker(diction):
    output_file = open('output.txt', 'wt')
    for item in sorted(diction):
        s = '{0} - {1}%\n'.format(item, diction[item])
        output_file.write(s)
    output_file.close()

wap = counter('D:/Projects/war_and_peace/wap/war.txt')
table_maker(wap)

