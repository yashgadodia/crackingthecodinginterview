def bruteforce(mylist,twosum):
    answerlist = []
    for i in range(len(mylist)-1):
        for j in range(i+1,len(mylist)):
            if mylist[i] + mylist[j] == twosum:
                answerlist.append(mylist[i])
                answerlist.append(mylist[j])
                

    print(answerlist)

# bruteforce([1,5,3,8,6,19],27)

def onepasshashtable(mylist,twosum):
    hashtable = {}

    for i in range(len(mylist)):
        if i == 0: #for first element, just put inside hashtable
            hashtable[mylist[i]] = i
        else:
            compliment = twosum - mylist[i]
            if compliment not in hashtable: #if not inside place number inside
                hashtable[mylist[i]] = i
                # print(hashtable)
            else: #inside
                print(mylist[hashtable[compliment]],mylist[i])
                


    # print(hashtable)  

# onepasshashtable([1,5,3,8,6,19],22)

#assuming a two-sum solution
def twopointers(mylist,total):

    p1 = 0 #p1 set to index 0 of the array
    p2 = (len(mylist) - 1) #p2 set to index -1 of array

    while mylist[p1] + mylist[p2] != total:
        while mylist[p1] + mylist[p2] > total:
            # print(mylist[p2])
            p2 -=1
        while mylist[p1] + mylist[p2] < total:
            # print(mylist[p1])
            p1 += 1

    print(mylist[p1],mylist[p2])
    print('hes')




# atwopointers([1,3,5,9,12,17,18,25,30],37)


# Given an array of integers, return the smallest set of indices of numbers such that they add up to a target number. 
# You may not use the same element twice.

# Examples:
# [1,2,6,3,17,82,23,234] -> 26
# Solution [3,6]

# [1,2,6,3,17,82,23,234] -> 40
# Solution [4,6]

# [1,2,6,3,17,82,23,234] -> 23
# Solution [6]


def main(myarray):
    myarray.sort()
    print(myarray)
main([1,2,6,3,17,82,23,234])