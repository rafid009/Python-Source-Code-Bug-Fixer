import numpy as np 

def function(x):

	x4 = 3
	c9 = 4
	paths = []
	try:
		if x4 > 5:
			c9 = x/c9
			paths.append(1)
		else:
			c9 = 2+3
			paths.append(2)
		if x < 7:
			x4 = x*x4
			paths.append(3)
		else:
			x4 = x4*3
			x = 5+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x4 = x**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))