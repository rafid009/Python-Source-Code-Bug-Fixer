import numpy as np 

def function(x):

	i5 = x
	c0 = x
	paths = []
	try:
		if i5 <= 1:
			i5 = 4*c0
			x = x+7
			paths.append(1)
		else:
			i5 = c0/i5
			paths.append(2)
		if c0 >= 3:
			i5 = i5+x
			paths.append(3)
		else:
			i5 = i5*3
			c0 = 9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c0 = x**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))