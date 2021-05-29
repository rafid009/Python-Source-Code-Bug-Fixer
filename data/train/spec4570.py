import numpy as np 

def function(x):

	w2 = 1
	z0 = 0
	paths = []
	try:
		if x > 7:
			x = x+1
			z0 = z0+3
			paths.append(1)
		else:
			z0 = 8+z0
			w2 = 2-z0
			z0 = x/z0
			paths.append(2)
		if x >= 0:
			x = x*x
			x = 1/x
			x = x+3
			paths.append(3)
		else:
			x = x+7
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		z0 = w2**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))