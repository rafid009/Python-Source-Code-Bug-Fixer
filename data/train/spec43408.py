import numpy as np 

def function(x):

	c6 = 6
	a1 = x
	paths = []
	try:
		if c6 < 7:
			c6 = c6/a1
			c6 = c6*4
			paths.append(1)
		else:
			x = 1+x
			paths.append(2)
		if x <= 7:
			c6 = 4-c6
			c6 = a1+c6
			x = x/7
			paths.append(3)
		else:
			c6 = c6+9
			c6 = 1-c6
			x = 3+x
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