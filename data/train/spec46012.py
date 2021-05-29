import numpy as np 

def function(x):

	z1 = 0
	x5 = x
	paths = []
	try:
		if x5 <= 5:
			x = x*7
			x = x+6
			paths.append(1)
		else:
			x5 = x5+x
			paths.append(2)
		if x5 <= 0:
			x = 8*x
			x = 3/x
			paths.append(3)
		else:
			x5 = x-x
			z1 = 5*8
			z1 = x5+x
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