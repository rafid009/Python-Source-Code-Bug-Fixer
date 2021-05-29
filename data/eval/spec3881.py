import numpy as np 

def function(x):

	z5 = x
	c0 = x
	paths = []
	try:
		if x >= 9:
			x = 5-x
			c0 = c0/2
			paths.append(1)
		else:
			x = c0/x
			c0 = z5+x
			paths.append(2)
		if x <= 2:
			x = 1*z5
			paths.append(3)
		else:
			z5 = 3-6
			x = z5/8
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		z5 = c0**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))