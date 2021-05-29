import numpy as np 

def function(x):

	y6 = 8
	c6 = 3
	paths = []
	try:
		if y6 >= 2:
			c6 = c6*2
			y6 = 3/5
			c6 = 4-c6
			paths.append(1)
		else:
			y6 = y6*2
			paths.append(2)
		if c6 >= 5:
			c6 = x*y6
			c6 = c6/x
			paths.append(3)
		else:
			y6 = 7-y6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))