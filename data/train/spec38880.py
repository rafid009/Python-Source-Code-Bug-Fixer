import numpy as np 

def function(x):

	w9 = 8
	y4 = x
	paths = []
	try:
		if x <= 6:
			y4 = 2/y4
			paths.append(1)
		else:
			w9 = 8+x
			x = x/y4
			paths.append(2)
		if x >= 9:
			y4 = y4+x
			x = x-6
			paths.append(3)
		else:
			y4 = 1-y4
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