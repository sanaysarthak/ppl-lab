import arithmetic_module

def main():
	print("Basic Arithmetic opertations using Module:-")
	
	x = 10
	y = 5

	print(f"{x} + {y} = {arithmetic_module.add(x, y)}")
	print(f"{x} - {y} = {arithmetic_module.subtract(x, y)}")
	print(f"{x} * {y} = {arithmetic_module.multiply(x, y)}")
	print(f"{x} / {y} = {arithmetic_module.divide(x, y)}")

if __name__ == "__main__":
	main()