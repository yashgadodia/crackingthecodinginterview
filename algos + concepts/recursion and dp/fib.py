# time complexity: 0(2**N)
# slowest way because it takes exponential time



def fib(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

print(fib(8))

