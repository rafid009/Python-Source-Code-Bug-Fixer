import numpy as np 

def function(x):

	e9 = 2
	c0 = 0
	paths = []
	try:
		if x >= 3:
			x = x-6
			e9 = x-4
			c0 = e9+c0
			paths.append(1)
		else:
			c0 = c0/x
			paths.append(2)
		if x > 2:
			c0 = 7+c0
			x = x*3
			paths.append(3)
		else:
			c0 = c0/5
			e9 = 2/e9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))