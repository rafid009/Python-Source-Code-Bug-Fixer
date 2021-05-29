import numpy as np 

def function(x):

	x5 = x
	c2 = 8
	paths = []
	try:
		if x5 > 4:
			x = x+4
			x = x-6
			x5 = 6-x5
			paths.append(1)
		else:
			c2 = c2*x
			c2 = 5-c2
			c2 = x+0
			paths.append(2)
		if x5 < 2:
			x5 = x5/c2
			x = 9*x
			x5 = 5+8
			paths.append(3)
		else:
			c2 = x*c2
			c2 = 3*x5
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