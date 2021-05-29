import numpy as np 

def function(x):

	y3 = 2
	n6 = 3
	paths = []
	try:
		if x < 6:
			y3 = y3-y3
			paths.append(1)
		else:
			n6 = n6*4
			paths.append(2)
		if n6 < 1:
			x = x/x
			paths.append(3)
		else:
			x = x-2
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