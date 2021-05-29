import numpy as np 

def function(x):

	x9 = 5
	c7 = 3
	paths = []
	try:
		if x > 7:
			x = 5-x
			x9 = 2-x9
			x9 = x9-6
			paths.append(1)
		else:
			x9 = 5*9
			paths.append(2)
		if c7 < 4:
			c7 = 2-x
			x = x/1
			paths.append(3)
		else:
			c7 = c7+2
			x = x+4
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