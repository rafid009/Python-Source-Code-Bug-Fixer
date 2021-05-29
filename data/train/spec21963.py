import numpy as np 

def function(x):

	c0 = x
	e0 = 1
	paths = []
	try:
		if c0 <= 3:
			x = e0/x
			x = c0+4
			paths.append(1)
		else:
			x = x-4
			c0 = c0+7
			paths.append(2)
		if e0 <= 4:
			c0 = c0+4
			c0 = 8+7
			x = x/8
			paths.append(3)
		else:
			e0 = x*e0
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