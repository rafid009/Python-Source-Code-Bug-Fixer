import numpy as np 

def function(x):

	x8 = 5
	n0 = 9
	paths = []
	try:
		if x < 3:
			n0 = n0-7
			x = x*n0
			x8 = x8-n0
			paths.append(1)
		else:
			x8 = x/x8
			paths.append(2)
		if n0 > 0:
			x = x/4
			paths.append(3)
		else:
			x8 = x8+n0
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