import numpy as np 

def function(x):

	e0 = 9
	c9 = 7
	paths = []
	try:
		if e0 > 0:
			x = x/6
			paths.append(1)
		else:
			c9 = 1-e0
			c9 = c9+4
			e0 = x*7
			paths.append(2)
		if e0 > 8:
			x = x+x
			x = x*1
			c9 = c9-c9
			paths.append(3)
		else:
			c9 = 1*c9
			c9 = 0+4
			x = x-0
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