import numpy as np 

def function(x):

	c4 = x
	y3 = 4
	paths = []
	try:
		if c4 < 9:
			y3 = y3-5
			x = 5*x
			paths.append(1)
		else:
			x = x-5
			x = c4+6
			paths.append(2)
		if c4 > 1:
			c4 = 6+c4
			paths.append(3)
		else:
			x = 0+x
			y3 = 0-7
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		c4 = y3**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))