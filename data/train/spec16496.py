import numpy as np 

def function(x):

	e7 = 8
	c4 = 6
	paths = []
	try:
		if x > 1:
			e7 = 5*e7
			e7 = e7-8
			c4 = x-c4
			paths.append(1)
		else:
			c4 = 6/e7
			e7 = 1-e7
			c4 = c4+e7
			paths.append(2)
		if x <= 2:
			x = 4-c4
			c4 = c4+3
			paths.append(3)
		else:
			e7 = x*4
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		c4 = c4**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))