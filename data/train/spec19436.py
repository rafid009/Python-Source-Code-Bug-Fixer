import numpy as np 

def function(x):

	w2 = x
	z0 = 1
	paths = []
	try:
		if w2 < 0:
			z0 = 1-z0
			x = w2/7
			paths.append(1)
		else:
			x = x-9
			z0 = 6-5
			z0 = z0+1
			paths.append(2)
		if w2 <= 3:
			x = x+7
			z0 = z0+2
			paths.append(3)
		else:
			x = x-x
			z0 = w2*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w2 = x**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))