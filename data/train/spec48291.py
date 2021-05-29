import numpy as np 

def function(x):

	f9 = x
	c8 = x
	paths = []
	try:
		if c8 < 4:
			x = 7/f9
			c8 = c8*3
			paths.append(1)
		else:
			x = x*7
			paths.append(2)
		if x <= 0:
			c8 = c8-x
			c8 = 9+5
			paths.append(3)
		else:
			x = x-c8
			f9 = f9*f9
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