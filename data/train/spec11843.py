import numpy as np 

def function(x):

	c0 = 2
	e3 = x
	paths = []
	try:
		if x < 4:
			x = c0-2
			e3 = e3*6
			paths.append(1)
		else:
			e3 = 6-x
			e3 = 8/e3
			paths.append(2)
		if c0 > 7:
			e3 = 8-9
			paths.append(3)
		else:
			c0 = c0+7
			e3 = 9*e3
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		c0 = e3**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))