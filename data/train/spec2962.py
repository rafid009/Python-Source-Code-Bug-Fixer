import numpy as np 

def function(x):

	y8 = 6
	z7 = 5
	paths = []
	try:
		if y8 <= 4:
			y8 = y8+9
			paths.append(1)
		else:
			z7 = 9-z7
			z7 = 0-z7
			y8 = 3+y8
			paths.append(2)
		if x < 2:
			x = 5/x
			x = x*y8
			y8 = 8+y8
			paths.append(3)
		else:
			y8 = y8+4
			x = 1-4
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		y8 = z7**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))