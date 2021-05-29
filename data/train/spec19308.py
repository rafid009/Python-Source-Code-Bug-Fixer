import numpy as np 

def function(x):

	b0 = x
	z6 = x
	paths = []
	try:
		if z6 <= 3:
			x = z6/x
			paths.append(1)
		else:
			b0 = b0/7
			z6 = 8-z6
			paths.append(2)
		if b0 > 0:
			z6 = 3+z6
			paths.append(3)
		else:
			z6 = 1/b0
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		x = b0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))