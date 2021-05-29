import numpy as np 

def function(x):

	c1 = x
	a4 = x
	paths = []
	try:
		if a4 < 7:
			c1 = 7+6
			paths.append(1)
		else:
			c1 = c1/a4
			c1 = a4*a4
			x = x-a4
			paths.append(2)
		if a4 >= 6:
			x = 7-8
			paths.append(3)
		else:
			c1 = c1*a4
			a4 = a4+x
			x = 4*x
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