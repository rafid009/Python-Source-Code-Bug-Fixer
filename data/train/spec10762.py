import numpy as np 

def function(x):

	u5 = x
	c6 = x
	paths = []
	try:
		if x <= 5:
			u5 = u5/3
			u5 = c6/u5
			paths.append(1)
		else:
			u5 = u5*5
			x = x+6
			paths.append(2)
		if x >= 8:
			x = 0-x
			x = x/4
			paths.append(3)
		else:
			c6 = c6*u5
			u5 = 1-3
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c6 = x**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))