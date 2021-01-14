def removeOuterParentheses(S):
    out = ''
    lst = []
    counta = 0
    countb = 0
    place = 0
    for i in range(len(S)-1):
        if S[i] == '(':
            counta += 1
        else:
            countb += 1
        if S[i] == ')' and S[i+1] == '(' and counta == countb:
            counta = 0
            countb = 0
            lst.append(S[place:i+1])
            place = i+1
        if i == (len(S)-2):
            lst.append(S[place:len(S)])
    for element in lst:
        out += element[1:len(element)-1]
    return out



Input = "()()"
print(removeOuterParentheses(Input))
