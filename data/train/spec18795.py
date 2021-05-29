import numpy as np 

def function(x):

	y7 = 8
	h6 = 0
	paths = []
	try:
		if h6 > 7:
			x = 2+6
			paths.append(1)
		else:
			x = x-7
			x = x-3
			paths.append(2)
		if x >= 3:
			y7 = 6+y7
			y7 = 8/y7
			paths.append(3)
		else:
			y7 = y7*7
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