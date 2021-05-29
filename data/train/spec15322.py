import numpy as np 

def function(x):

	c5 = 7
	y4 = x
	paths = []
	try:
		if x <= 2:
			y4 = 2/c5
			paths.append(1)
		else:
			y4 = 0+1
			y4 = 1-4
			paths.append(2)
		if x >= 7:
			y4 = 4/x
			x = 0*6
			paths.append(3)
		else:
			x = 2+3
			x = x*5
			c5 = 0+c5
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		c5 = y4**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))