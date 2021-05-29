import numpy as np 

def function(x):

	c0 = 0
	g7 = x
	x = x
	paths = []
	try:
		if x <= 2:
			x = 8*x
			x = 4-x
			x = x+6
			paths.append(1)
		else:
			c0 = g7+9
			paths.append(2)
		if g7 < 3:
			x = x*2
			c0 = 2*9
			paths.append(3)
		else:
			x = x*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c0 = x**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))