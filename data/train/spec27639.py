import numpy as np 

def function(x):

	y0 = x
	c8 = x
	paths = []
	try:
		if x < 3:
			c8 = 9/1
			c8 = c8/3
			c8 = 1+7
			paths.append(1)
		else:
			y0 = 2/y0
			x = x-5
			c8 = c8-2
			paths.append(2)
		if x <= 9:
			y0 = c8*5
			paths.append(3)
		else:
			c8 = y0-5
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))