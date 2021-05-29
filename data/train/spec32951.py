import numpy as np 

def function(x):

	z7 = x
	c8 = 5
	paths = []
	try:
		if x >= 9:
			x = 8*z7
			x = c8*6
			paths.append(1)
		else:
			c8 = x+5
			x = x*c8
			paths.append(2)
		if c8 < 3:
			z7 = 5/x
			paths.append(3)
		else:
			z7 = z7-x
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		z7 = z7**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))