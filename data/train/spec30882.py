import numpy as np 

def function(x):

	e5 = 4
	c8 = 8
	paths = []
	try:
		if x <= 4:
			e5 = 0-e5
			x = x*5
			paths.append(1)
		else:
			e5 = 0*6
			paths.append(2)
		if c8 >= 2:
			x = x/5
			c8 = c8-8
			c8 = c8-0
			paths.append(3)
		else:
			c8 = 6/x
			c8 = 2+c8
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