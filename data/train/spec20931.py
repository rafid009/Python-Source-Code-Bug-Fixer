import numpy as np 

def function(x):

	z7 = 0
	c7 = 3
	paths = []
	try:
		if x < 4:
			x = x*7
			x = x/7
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if z7 > 4:
			c7 = c7+z7
			paths.append(3)
		else:
			c7 = c7-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z7 = x**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))