import numpy as np 

def function(x):

	c1 = 1
	v0 = 5
	x = 5
	paths = []
	try:
		if c1 < 9:
			v0 = 1-8
			c1 = c1+6
			paths.append(1)
		else:
			c1 = 1*c1
			paths.append(2)
		if c1 >= 8:
			x = x*9
			c1 = c1-c1
			c1 = x/c1
			paths.append(3)
		else:
			x = 8/8
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		c1 = v0**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))