import numpy as np 

def function(x):

	c9 = x
	y0 = 6
	paths = []
	try:
		if x <= 2:
			c9 = c9*c9
			y0 = y0+x
			c9 = y0+x
			paths.append(1)
		else:
			y0 = y0+5
			c9 = 6-5
			paths.append(2)
		if c9 > 0:
			y0 = 4-y0
			y0 = y0-5
			paths.append(3)
		else:
			c9 = 2+c9
			x = x+y0
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		c9 = c9**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))