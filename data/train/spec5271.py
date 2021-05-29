import numpy as np 

def function(x):

	y6 = 2
	c7 = x
	paths = []
	try:
		if y6 < 8:
			y6 = x*1
			c7 = 8-3
			paths.append(1)
		else:
			c7 = 0-c7
			y6 = y6-6
			c7 = 6/c7
			paths.append(2)
		if c7 > 1:
			x = 2*x
			y6 = y6*7
			y6 = y6+c7
			paths.append(3)
		else:
			y6 = 1*7
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		c7 = y6**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))