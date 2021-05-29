import numpy as np 

def function(x):

	c8 = x
	x8 = 7
	paths = []
	try:
		if x >= 1:
			c8 = c8/7
			paths.append(1)
		else:
			c8 = x8/c8
			x = 8+c8
			c8 = x8/2
			paths.append(2)
		if c8 <= 5:
			x8 = x8+0
			paths.append(3)
		else:
			c8 = 3+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x8 = x**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))