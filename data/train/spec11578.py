import numpy as np 

def function(x):

	c4 = 3
	x5 = x
	x = x
	paths = []
	try:
		if x < 9:
			x = x+x
			c4 = 1+c4
			paths.append(1)
		else:
			x = x/9
			c4 = 8+c4
			paths.append(2)
		if c4 > 0:
			x5 = x5/3
			c4 = c4/x5
			x5 = 1*9
			paths.append(3)
		else:
			c4 = 0/5
			c4 = 0/c4
			x5 = 3/6
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