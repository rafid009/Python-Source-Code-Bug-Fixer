import numpy as np 

def function(x):

	c2 = 9
	c3 = x
	paths = []
	try:
		if x < 0:
			x = 4+x
			c3 = c3-x
			paths.append(1)
		else:
			c2 = c2*c3
			paths.append(2)
		if c2 <= 9:
			c2 = c3*c2
			c2 = c2*x
			paths.append(3)
		else:
			x = 3+x
			x = 3-x
			c3 = c3+x
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