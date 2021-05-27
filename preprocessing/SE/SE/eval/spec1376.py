import numpy as np 

def function(x):

	n1 = 8
	c8 = 1
	paths = []
	try:
		if n1 > 0:
			x = x+6
			paths.append(1)
		else:
			x = c8+6
			c8 = c8+c8
			n1 = 1*n1
			paths.append(2)
		if c8 < 8:
			n1 = 8*9
			paths.append(3)
		else:
			c8 = c8*9
			n1 = n1/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))