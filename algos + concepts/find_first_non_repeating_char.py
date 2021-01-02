"""
Finds the first character that does not repeat anywhere in the input string
If all characters are repeated, return 0
Given "apple", the answer is "a"
Given "racecars", the answer is "e"
Given "ababdc", the answer is "d"
"""

def find_first(inputstr):
    # answerletter = ''
    # correctletter = False
    # for i in range(len(inputstr)-1):
    #     for j in range(i+1,len(inputstr)):
    #         if inputstr[i] == inputstr[j]:
    #             # print(inputstr[j])
    #             correctletter = True
    #         print(inputstr[j])
    #     if correctletter == False:
    #         print(inputstr[i])
    #         answerletter += inputstr[i]
    # if len(answerletter) == 0:
    #     return 0
    # return answerletter

    mydict = {}
    for letter in inputstr:
        if letter not in mydict:
            mydict[letter] = 0
        else:
            mydict[letter] += 1
    for pair in mydict.items():
        if pair[1] == 0:
            return pair[0]
    return 0

if __name__ == '__main__':
    from mark import mark

    test_cases = [
        ('racecar', 'e'),
        ('apple', 'a'),
        ('ababdc', 'd'),
        ('xxyyzz', 0),
        ('abc', 'a')
    ]

    mark(find_first, test_cases)