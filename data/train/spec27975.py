import numpy as np 

def function(x):

	c0 = 5
	w8 = 5
	paths = []
	try:
		if c0 > 2:
			x = 0+4
			c0 = c0*7
			paths.append(1)
		else:
			x = 7+4
			paths.append(2)
		if c0 >= 7:
			c0 = 6-c0
			paths.append(3)
		else:
			c0 = w8/8
			w8 = w8*9
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		c0 = c0**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))