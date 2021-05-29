import numpy as np 

def function(x):

	n4 = x
	y0 = 3
	paths = []
	try:
		if n4 < 0:
			n4 = x-n4
			n4 = 3+8
			paths.append(1)
		else:
			y0 = y0+x
			y0 = y0-1
			paths.append(2)
		if y0 < 0:
			y0 = 3/y0
			x = 0*n4
			y0 = x-4
			paths.append(3)
		else:
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n4 = x**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))