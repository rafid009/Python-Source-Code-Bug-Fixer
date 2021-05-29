import numpy as np 

def function(x):

	u9 = 5
	c4 = 0
	x = x
	paths = []
	try:
		if c4 > 8:
			x = x+c4
			paths.append(1)
		else:
			c4 = x+c4
			x = 5+x
			u9 = 5*7
			paths.append(2)
		if c4 < 8:
			c4 = 4-c4
			paths.append(3)
		else:
			c4 = c4-x
			x = 7/3
			c4 = c4-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c4 = x**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))