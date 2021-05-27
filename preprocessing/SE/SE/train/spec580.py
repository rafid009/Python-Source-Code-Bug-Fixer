import numpy as np 

def function(x):

	w1 = 9
	z0 = x
	paths = []
	try:
		if x >= 5:
			x = 8+w1
			z0 = 1/9
			w1 = 5*w1
			paths.append(1)
		else:
			x = 2+x
			x = x-5
			paths.append(2)
		if w1 >= 6:
			z0 = z0*7
			paths.append(3)
		else:
			z0 = z0+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w1 = x**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))