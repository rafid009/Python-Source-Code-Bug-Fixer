import numpy as np 

def function(x):

	j9 = x
	c9 = x
	paths = []
	try:
		if c9 <= 0:
			c9 = 0+4
			paths.append(1)
		else:
			j9 = j9*j9
			paths.append(2)
		if j9 < 3:
			x = x*j9
			c9 = c9*3
			x = 6-x
			paths.append(3)
		else:
			c9 = c9/j9
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