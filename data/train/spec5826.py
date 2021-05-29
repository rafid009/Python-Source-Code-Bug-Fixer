import numpy as np 

def function(x):

	c6 = x
	x9 = 9
	paths = []
	try:
		if c6 > 8:
			c6 = 8*c6
			x = x+x
			paths.append(1)
		else:
			c6 = 6+c6
			x9 = x9/8
			x9 = x9-4
			paths.append(2)
		if x9 < 9:
			x9 = 4-9
			x = c6/6
			paths.append(3)
		else:
			x = 7-x
			x9 = 7/x9
			x9 = 6/x9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x9 = x**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))