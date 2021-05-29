import numpy as np 

def function(x):

	v4 = x
	c2 = x
	paths = []
	try:
		if c2 <= 3:
			x = x*9
			c2 = 2+c2
			paths.append(1)
		else:
			x = x-5
			paths.append(2)
		if v4 > 4:
			v4 = 4/v4
			paths.append(3)
		else:
			c2 = 2/c2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c2 = x**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))