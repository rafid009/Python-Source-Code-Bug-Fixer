import numpy as np 

def function(x):

	c5 = 2
	a0 = 4
	paths = []
	try:
		if x < 2:
			a0 = 2-6
			c5 = 5/c5
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if a0 < 1:
			a0 = c5*a0
			x = x+8
			paths.append(3)
		else:
			a0 = a0/c5
			c5 = x*c5
			a0 = a0/2
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