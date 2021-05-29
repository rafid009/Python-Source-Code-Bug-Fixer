import numpy as np 

def function(x):

	c9 = 1
	u0 = 0
	paths = []
	try:
		if c9 > 0:
			u0 = u0+c9
			c9 = c9*c9
			paths.append(1)
		else:
			x = x+9
			paths.append(2)
		if c9 < 4:
			x = x+3
			paths.append(3)
		else:
			x = u0*x
			c9 = x+c9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u0 = x**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))