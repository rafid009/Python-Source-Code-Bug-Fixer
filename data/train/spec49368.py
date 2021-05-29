import numpy as np 

def function(x):

	z6 = 7
	w1 = x
	paths = []
	try:
		if w1 <= 3:
			z6 = x*7
			z6 = 4+z6
			x = 6+x
			paths.append(1)
		else:
			z6 = 0-z6
			w1 = z6*w1
			x = 5*x
			paths.append(2)
		if x >= 3:
			x = w1*x
			z6 = z6-z6
			x = 2-x
			paths.append(3)
		else:
			x = 3*x
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