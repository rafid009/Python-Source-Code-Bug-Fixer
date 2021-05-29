import numpy as np 

def function(x):

	c9 = x
	u1 = 0
	paths = []
	try:
		if u1 < 7:
			u1 = u1+0
			x = 1/x
			paths.append(1)
		else:
			c9 = c9*c9
			x = 4-x
			paths.append(2)
		if u1 < 0:
			c9 = c9/6
			paths.append(3)
		else:
			u1 = u1+3
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