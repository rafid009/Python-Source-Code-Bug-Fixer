import numpy as np 

def function(x):

	y7 = 0
	b4 = x
	paths = []
	try:
		if y7 >= 3:
			b4 = b4-3
			x = 3/x
			paths.append(1)
		else:
			x = y7-x
			b4 = 3+3
			paths.append(2)
		if y7 < 3:
			y7 = x-4
			paths.append(3)
		else:
			y7 = 7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))