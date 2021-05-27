import numpy as np 

def function(x):

	a8 = x
	c5 = 3
	paths = []
	try:
		if a8 >= 4:
			c5 = 5*c5
			a8 = a8-1
			a8 = 9*5
			paths.append(1)
		else:
			c5 = 3*c5
			paths.append(2)
		if c5 < 9:
			a8 = a8/x
			paths.append(3)
		else:
			a8 = x*c5
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		c5 = a8**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))