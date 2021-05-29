import numpy as np 

def function(x):

	z7 = x
	o0 = x
	paths = []
	try:
		if x <= 1:
			z7 = 3-2
			paths.append(1)
		else:
			z7 = z7-6
			x = x/8
			paths.append(2)
		if z7 > 2:
			x = 6/x
			paths.append(3)
		else:
			z7 = z7-4
			z7 = 7/9
			z7 = 8+z7
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