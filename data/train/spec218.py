import numpy as np 

def function(x):

	f7 = x
	c6 = 6
	paths = []
	try:
		if c6 >= 6:
			c6 = c6*x
			x = x/4
			c6 = c6-4
			paths.append(1)
		else:
			c6 = x*9
			f7 = 6*x
			x = 7/x
			paths.append(2)
		if f7 >= 2:
			x = x/f7
			c6 = f7*x
			f7 = 0*f7
			paths.append(3)
		else:
			x = 1/x
			f7 = 2*x
			f7 = c6/f7
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		c6 = f7**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))