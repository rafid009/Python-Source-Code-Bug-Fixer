import numpy as np 

def function(x):

	v1 = 4
	c1 = 8
	paths = []
	try:
		if x <= 7:
			x = 2*x
			x = x+4
			v1 = 4-v1
			paths.append(1)
		else:
			v1 = v1/6
			x = x-v1
			paths.append(2)
		if x >= 3:
			c1 = c1+8
			c1 = c1+5
			c1 = 1/9
			paths.append(3)
		else:
			c1 = 3*c1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))