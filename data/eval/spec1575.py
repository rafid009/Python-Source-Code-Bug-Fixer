import numpy as np 

def function(x):

	b5 = 3
	z5 = 9
	paths = []
	try:
		if b5 > 1:
			z5 = z5+z5
			b5 = b5*b5
			paths.append(1)
		else:
			x = 6/x
			x = x*5
			paths.append(2)
		if x < 0:
			x = x+3
			b5 = b5*6
			b5 = 8-b5
			paths.append(3)
		else:
			x = 7+8
			x = z5/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z5 = x**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))