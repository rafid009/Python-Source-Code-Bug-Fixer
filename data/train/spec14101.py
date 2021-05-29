import numpy as np 

def function(x):

	c7 = x
	y2 = x
	paths = []
	try:
		if c7 < 3:
			x = 1+x
			paths.append(1)
		else:
			c7 = c7-x
			y2 = y2-x
			c7 = 0/x
			paths.append(2)
		if c7 > 9:
			c7 = c7-7
			c7 = 3+6
			paths.append(3)
		else:
			y2 = 7/x
			y2 = y2/y2
			y2 = y2+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y2 = x**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))