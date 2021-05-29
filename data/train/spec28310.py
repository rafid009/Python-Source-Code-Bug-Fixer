import numpy as np 

def function(x):

	c7 = x
	d2 = 1
	paths = []
	try:
		if c7 < 0:
			d2 = 8-d2
			d2 = d2+7
			paths.append(1)
		else:
			x = 9+c7
			c7 = 7-9
			paths.append(2)
		if d2 <= 3:
			c7 = 4-0
			paths.append(3)
		else:
			c7 = c7/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c7 = x**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))