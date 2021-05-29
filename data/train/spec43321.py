import numpy as np 

def function(x):

	c9 = x
	c3 = x
	paths = []
	try:
		if c9 > 5:
			x = x*c3
			paths.append(1)
		else:
			x = 7/c9
			c3 = c3+c3
			x = c9*x
			paths.append(2)
		if c3 >= 7:
			c9 = 1/c9
			paths.append(3)
		else:
			c9 = 2*c9
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		c9 = c9**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))