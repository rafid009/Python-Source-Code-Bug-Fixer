import numpy as np 

def function(x):

	c5 = x
	e7 = x
	paths = []
	try:
		if c5 >= 2:
			x = 7*8
			x = 7/x
			paths.append(1)
		else:
			x = x*7
			paths.append(2)
		if x > 7:
			c5 = c5-2
			paths.append(3)
		else:
			e7 = e7/3
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		c5 = e7**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))