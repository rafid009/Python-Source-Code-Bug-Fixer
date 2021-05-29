import numpy as np 

def function(x):

	y1 = 2
	c0 = 2
	paths = []
	try:
		if c0 <= 2:
			y1 = c0-4
			paths.append(1)
		else:
			x = c0+x
			paths.append(2)
		if x >= 1:
			y1 = y1-9
			x = x+7
			paths.append(3)
		else:
			y1 = 6-9
			y1 = y1/c0
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		c0 = y1**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))