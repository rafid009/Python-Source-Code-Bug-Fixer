import numpy as np 

def function(x):

	c9 = 6
	d2 = x
	paths = []
	try:
		if x > 3:
			c9 = 1/7
			x = c9+6
			d2 = x*2
			paths.append(1)
		else:
			d2 = d2+2
			paths.append(2)
		if x >= 2:
			c9 = 5+c9
			c9 = c9-7
			paths.append(3)
		else:
			x = 0-x
			x = x*d2
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