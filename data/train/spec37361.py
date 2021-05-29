import numpy as np 

def function(x):

	h1 = 3
	z7 = x
	x = x
	paths = []
	try:
		if x >= 3:
			x = h1-5
			x = x+3
			z7 = x-4
			paths.append(1)
		else:
			z7 = z7-z7
			z7 = z7-9
			paths.append(2)
		if x >= 2:
			x = x-1
			h1 = 0+5
			x = 9+x
			paths.append(3)
		else:
			z7 = z7+z7
			z7 = 0*z7
			h1 = x+0
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