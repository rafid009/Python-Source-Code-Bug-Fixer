import numpy as np 

def function(x):

	h8 = 1
	z7 = 4
	paths = []
	try:
		if x >= 3:
			h8 = h8/z7
			z7 = 4+z7
			z7 = 6/z7
			paths.append(1)
		else:
			h8 = z7*h8
			z7 = 5*z7
			paths.append(2)
		if z7 < 6:
			x = x*9
			z7 = 3+5
			paths.append(3)
		else:
			h8 = z7-h8
			z7 = 2-6
			z7 = 3-h8
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		x = z7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))