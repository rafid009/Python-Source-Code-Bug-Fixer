import numpy as np 

def function(x):

	c7 = x
	n6 = x
	paths = []
	try:
		if n6 > 9:
			x = x*4
			x = x-5
			x = x/5
			paths.append(1)
		else:
			x = x/3
			paths.append(2)
		if n6 > 5:
			c7 = 9-x
			x = x+c7
			paths.append(3)
		else:
			n6 = n6/8
			x = 2*n6
			x = 2*c7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c7 = x**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))