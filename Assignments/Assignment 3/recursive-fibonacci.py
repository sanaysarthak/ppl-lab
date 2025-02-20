# Recursive function to generate nth fibonacci number
def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

print("First 15 Fibonacci numbers are:-")
for i in range(15):
	print(fibonacci(i), end = ' ')