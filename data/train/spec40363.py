import numpy as np 

def function(x):

	a4 = 4
	c7 = 9
	paths = []
	try:
		if c7 < 2:
			c7 = x+6
			c7 = x-c7
			x = c7/x
			paths.append(1)
		else:
			x = x-8
			c7 = a4*9
			paths.append(2)
		if x >= 9:
			c7 = 8+x
			a4 = 8/1
			x = 2*x
			paths.append(3)
		else:
			a4 = a4*a4
			a4 = a4-7
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