import numpy as np 

def function(x):

	c2 = x
	x7 = 8
	paths = []
	try:
		if x7 < 8:
			c2 = c2*6
			x = 0-x
			c2 = c2/6
			paths.append(1)
		else:
			x7 = x7*x
			c2 = c2+7
			x7 = x7+x
			paths.append(2)
		if x < 2:
			x7 = 5-x
			x7 = x7+8
			paths.append(3)
		else:
			x7 = 3-1
			c2 = 3/x
			x7 = x7-9
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x7 = x7**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))