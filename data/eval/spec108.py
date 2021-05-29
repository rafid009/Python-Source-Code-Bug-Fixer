import numpy as np 

def function(x):

	c3 = 8
	n8 = 3
	paths = []
	try:
		if n8 > 3:
			c3 = c3*7
			x = 1*x
			paths.append(1)
		else:
			n8 = n8+6
			paths.append(2)
		if n8 < 0:
			c3 = c3/3
			n8 = 8/x
			paths.append(3)
		else:
			n8 = 1*x
			x = 6-x
			c3 = 6-c3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))