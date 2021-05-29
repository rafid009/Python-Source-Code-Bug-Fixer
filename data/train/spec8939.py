import numpy as np 

def function(x):

	c4 = x
	m1 = 3
	paths = []
	try:
		if m1 < 8:
			x = 7/6
			x = c4*6
			paths.append(1)
		else:
			x = x/x
			c4 = m1-c4
			c4 = c4-2
			paths.append(2)
		if x >= 1:
			c4 = 0-c4
			paths.append(3)
		else:
			x = 7*x
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