import numpy as np 

def function(x):

	n0 = x
	z9 = x
	paths = []
	try:
		if n0 < 2:
			n0 = n0/2
			n0 = z9-n0
			paths.append(1)
		else:
			n0 = 6*x
			n0 = n0/6
			z9 = z9*8
			paths.append(2)
		if n0 > 4:
			z9 = 2*4
			x = 8-8
			paths.append(3)
		else:
			n0 = 9-7
			z9 = 9-z9
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