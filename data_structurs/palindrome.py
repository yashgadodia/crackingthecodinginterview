def is_palindrom():
	mystr = 'racecar'
	palin = 0 #set palin to false
	# print(mystr[-0])
	for i in range(len(mystr)):
		# print(i)
		# print('from back',mystr[-i-1])
		if mystr[i] == mystr[-i-1]:
			palin = 0
		else:
			palin = 1
			break

	if palin == 0 :
		print('is palin')
	else:
		print('not palin')

# is_palindrom()

def ispalin2():
	is_palin = True
	for i in range(0, len(word)//2):
		if word[i] != word[len[word] -1 -i]:
			is_palin = False
			break

emptystr = ''
mystr = 'Hello!'
for i in range(len(mystr)):
	emptystr += mystr[i]
	print(emptystr)

lenrows = []
for i in range(len(mystr)):
	lenrows.append(i+1)
for j in range(lenrows[-1],0,-1):
	print(mystr[:j])

mystr = 'helllooo'
print('here',mystr[1:4])



x = 'papaya'
# print(x[1:4])





