import string


def freqAlphabets(s):
    code = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10#', '11#', '12#', '13#', '14#', '15#', '16#', '17#', '18#',
            '19#', '20#', '21#', '22#', '23#', '24#', '25#', '26#']
    decode = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
    res = []
    for i in range(0, len(s), 1):
        check = None
        if i < (len(s)-2) and s[i+2] == '#':
            check = s[i] + s[i + 1] + s[i + 2]
        elif i < (len(s)-1) and s[i+1] == '#':
            pass
        else:
            check = s[i]
        for j in range(0, len(code), 1):
            if check == code[j]:
                res.append(decode[j])
                break
    return ''.join(res)


s = '12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#'
out = freqAlphabets(s)
print(out)
