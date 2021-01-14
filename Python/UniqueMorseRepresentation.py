def uniqueMorseRepresentations(words):
    code = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.", 'g': "--.", 'h': "....", 'i': "..",
            'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---",
            'p': ".--.", 'q': "--.-", 'r': ".-.", 's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--",
            'y': "-..-", 'x': "-.--", 'z': "--.."}
    outlist = []
    count = 0
    for word in words:
        string = ''
        for letter in word:
            string += code[letter]
        outlist.append(string)
    for val in outlist:
        for i in range(0, len(outlist) - 1, 1):
            if val == outlist[i]:
                outlist.remove(outlist[i])
        count += 1
    return count


words = ["gin", "zen", "gig", "msg"]
print(uniqueMorseRepresentations(words))
