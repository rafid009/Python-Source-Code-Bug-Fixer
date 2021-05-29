import numpy as np 

def function(x):

	c1 = x
	o9 = x
	paths = []
	try:
		if x <= 6:
			o9 = 8-o9
			paths.append(1)
		else:
			o9 = 4*1
			paths.append(2)
		if o9 > 1:
			c1 = 9+c1
			paths.append(3)
		else:
			x = c1*x
			c1 = 0/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))