import numpy as np 

def function(x):

	c8 = x
	x3 = 8
	paths = []
	try:
		if c8 >= 9:
			x = x-c8
			x = x-5
			x = 0/x
			paths.append(1)
		else:
			x3 = c8+x3
			c8 = 5/x
			x = c8/7
			paths.append(2)
		if c8 < 6:
			x3 = c8*6
			x3 = 0/x
			paths.append(3)
		else:
			c8 = c8/6
			x3 = 8+c8
			x = 3-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x3 = x**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))