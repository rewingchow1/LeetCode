def reverse(phrase, new_phrase=None):
    if new_phrase is None:
        new_phrase = ''
    new_phrase += phrase[len(phrase) - 1]
    phrase = phrase[:-1]
    if phrase == '':
        return new_phrase
    return reverse(phrase, new_phrase)


line = 'Failure'
print(reverse(line))

