import numpy as np 

def function(x):

	c8 = 4
	y6 = 1
	paths = []
	try:
		if x >= 4:
			x = 6*2
			paths.append(1)
		else:
			c8 = 9/c8
			y6 = 0-x
			paths.append(2)
		if x >= 3:
			c8 = c8*x
			x = x/1
			x = 8+8
			paths.append(3)
		else:
			x = x-3
			x = x+x
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		x = y6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))