import numpy as np 

def function(x):

	a7 = x
	c1 = 1
	paths = []
	try:
		if a7 >= 2:
			a7 = 1-a7
			paths.append(1)
		else:
			c1 = c1+c1
			c1 = c1/a7
			x = x/8
			paths.append(2)
		if c1 < 2:
			a7 = 1-a7
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a7 = x**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))