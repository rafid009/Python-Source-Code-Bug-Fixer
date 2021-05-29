import numpy as np 

def function(x):

	c8 = 9
	c3 = 5
	paths = []
	try:
		if c3 <= 6:
			c8 = 7-x
			paths.append(1)
		else:
			c3 = c8-c3
			paths.append(2)
		if x >= 6:
			c3 = 8-x
			x = 9-c3
			paths.append(3)
		else:
			x = x+5
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		c8 = c3**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))