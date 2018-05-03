# factorial program

def factorial(n, product = 1):
	product *= n
	n = n-1
	if n <= 0:
		return product
	return factorial(n, product)

print(factorial(10))