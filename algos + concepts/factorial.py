# time complexity: 0(2**N)
# slowest way because it takes exponential time



def factorial_recursive(n):
	if n == 1:
		return 1
	else:
		return n*factorial_recursive(n-1)

print(factorial_recursive(6))