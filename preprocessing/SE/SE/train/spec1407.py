import numpy as np 

def function(x):

	a9 = 4
	c3 = x
	paths = []
	try:
		if x >= 5:
			c3 = 9-c3
			c3 = a9*c3
			a9 = a9*3
			paths.append(1)
		else:
			c3 = a9/a9
			paths.append(2)
		if c3 < 7:
			c3 = a9+x
			a9 = 7*a9
			paths.append(3)
		else:
			c3 = c3-7
			c3 = 8+c3
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