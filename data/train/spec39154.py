import numpy as np 

def function(x):

	c4 = 5
	c7 = 5
	paths = []
	try:
		if x <= 8:
			x = 3-c4
			x = 6+x
			paths.append(1)
		else:
			c4 = 8*c4
			c7 = 2*c7
			paths.append(2)
		if c7 > 3:
			x = x*6
			x = 3-7
			c4 = c4-1
			paths.append(3)
		else:
			c7 = c7*9
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