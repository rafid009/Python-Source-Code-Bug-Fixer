import numpy as np 

def function(x):

	c4 = 2
	x7 = 4
	x = 4
	paths = []
	try:
		if x7 > 5:
			c4 = 6+x
			paths.append(1)
		else:
			c4 = c4+x
			x7 = x7+3
			paths.append(2)
		if c4 <= 5:
			c4 = 4+7
			x = 5/x
			paths.append(3)
		else:
			x7 = 9/2
			c4 = c4-4
			x = x-x7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x7 = x**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))