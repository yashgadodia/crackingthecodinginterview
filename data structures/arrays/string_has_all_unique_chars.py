# Given a string, determine if the string has all unique characters.

# 1) brute force it 

def main(str):
    for i in range(len(str)):
        for j in range(i+1, len(str)):
            if (str[i] == str[j]):
                return False
    return True

print(main('asdfghj'))

# 2) use ASCII values of characters (sorting)

def uniqueChars(str):

    #first sort it
    sortedStr = sorted(str)

    for i in range(len(sortedStr)-1):

        #if at any time 2 adjacent elements are equal return false
        if (sortedStr[i] == sortedStr[i+1]):
            return False
    
    return True

print(uniqueChars('asdfghjkl'))

# Bonus: what if you cannot use additional data strucutures?




