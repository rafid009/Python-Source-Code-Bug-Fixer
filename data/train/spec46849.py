import numpy as np 

def function(x):

	e8 = 6
	c0 = x
	paths = []
	try:
		if c0 > 9:
			c0 = x+c0
			c0 = 0-c0
			paths.append(1)
		else:
			e8 = e8/1
			paths.append(2)
		if c0 <= 3:
			c0 = 9+c0
			paths.append(3)
		else:
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e8 = x**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))