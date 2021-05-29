import numpy as np 

def function(x):

	c4 = x
	e0 = 4
	paths = []
	try:
		if c4 > 5:
			x = x+0
			c4 = c4+c4
			c4 = 9*2
			paths.append(1)
		else:
			e0 = e0-e0
			e0 = x+e0
			paths.append(2)
		if x >= 0:
			c4 = e0*c4
			c4 = c4+6
			paths.append(3)
		else:
			c4 = 4*c4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))