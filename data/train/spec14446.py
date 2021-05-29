import numpy as np 

def function(x):

	y0 = 8
	n5 = 0
	paths = []
	try:
		if y0 > 3:
			n5 = n5*n5
			paths.append(1)
		else:
			n5 = 3+3
			paths.append(2)
		if x < 3:
			n5 = n5/6
			y0 = 1+y0
			paths.append(3)
		else:
			x = x*6
			y0 = y0/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))