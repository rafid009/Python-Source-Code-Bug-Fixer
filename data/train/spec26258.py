import numpy as np 

def function(x):

	x3 = 1
	c9 = x
	paths = []
	try:
		if x3 < 4:
			c9 = c9-9
			paths.append(1)
		else:
			x = x-0
			paths.append(2)
		if x > 8:
			x = x-4
			c9 = 7+c9
			x3 = x3+0
			paths.append(3)
		else:
			x3 = x+4
			x = x-6
			x = x/x3
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		c9 = x3**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))