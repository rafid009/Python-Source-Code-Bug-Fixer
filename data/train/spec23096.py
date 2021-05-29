import numpy as np 

def function(x):

	c2 = 6
	c8 = 4
	paths = []
	try:
		if x <= 3:
			c2 = c2+c2
			paths.append(1)
		else:
			x = c2-c8
			c8 = 2-c2
			x = c2/5
			paths.append(2)
		if c8 >= 9:
			c2 = 3*1
			paths.append(3)
		else:
			x = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c8 = x**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))