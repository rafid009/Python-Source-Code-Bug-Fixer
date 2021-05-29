import numpy as np 

def function(x):

	c9 = x
	n1 = x
	paths = []
	try:
		if n1 < 7:
			c9 = c9/c9
			paths.append(1)
		else:
			x = 2-x
			n1 = n1/9
			paths.append(2)
		if n1 >= 6:
			x = x*1
			c9 = 4*c9
			paths.append(3)
		else:
			n1 = n1+n1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c9 = x**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))