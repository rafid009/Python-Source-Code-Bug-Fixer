import numpy as np 

def function(x):

	c6 = 8
	e5 = x
	paths = []
	try:
		if x >= 5:
			x = 0+x
			e5 = 9*e5
			e5 = 0*e5
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if c6 > 5:
			c6 = c6-c6
			paths.append(3)
		else:
			c6 = c6*9
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		c6 = e5**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))