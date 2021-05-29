import numpy as np 

def function(x):

	h0 = x
	z8 = 5
	paths = []
	try:
		if z8 >= 7:
			z8 = 9/1
			z8 = x-z8
			paths.append(1)
		else:
			z8 = z8+0
			z8 = z8*3
			paths.append(2)
		if z8 > 7:
			z8 = z8/4
			x = x-x
			paths.append(3)
		else:
			z8 = 2-7
			x = 6*h0
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		x = h0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))