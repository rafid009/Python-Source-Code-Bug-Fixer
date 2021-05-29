import numpy as np 

def function(x):

	h4 = 2
	z9 = x
	x = 4
	paths = []
	try:
		if x > 7:
			x = x+9
			z9 = 7/z9
			h4 = h4+4
			paths.append(1)
		else:
			h4 = 4+h4
			paths.append(2)
		if z9 >= 6:
			z9 = z9/x
			x = x-z9
			x = z9*x
			paths.append(3)
		else:
			z9 = 6/z9
			z9 = z9*8
			x = x/x
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