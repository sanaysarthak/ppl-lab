# Write a Python script that uses a lambda function combined with the map() and filter() functions to process a list of numbers.
# The script should square each number in the list and then filter out the squares that are even. Print the final list of odd squares.  

numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_squares = list(filter(lambda x: x % 2 != 0, map(lambda x: x ** 2, numlist)))
print("Odd squares:", odd_squares)