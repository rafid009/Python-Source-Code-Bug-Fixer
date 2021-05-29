import numpy as np 

def function(x):

	y5 = x
	c5 = 3
	paths = []
	try:
		if c5 > 8:
			x = 3/x
			x = 3-y5
			paths.append(1)
		else:
			c5 = c5-8
			paths.append(2)
		if y5 > 6:
			y5 = y5+7
			paths.append(3)
		else:
			y5 = y5-2
			x = y5*y5
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		x = y5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))