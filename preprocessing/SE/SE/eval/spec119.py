import numpy as np 

def function(x):

	c6 = x
	c9 = x
	paths = []
	try:
		if c9 < 4:
			c6 = c6+x
			paths.append(1)
		else:
			c6 = c6*2
			paths.append(2)
		if c6 >= 0:
			c6 = 7/c6
			c6 = c6/x
			paths.append(3)
		else:
			c9 = c9/c9
			x = x-1
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		c6 = c6**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))