import numpy as np 

def function(x):

	w3 = x
	z2 = 5
	paths = []
	try:
		if x < 3:
			z2 = x/z2
			w3 = w3*x
			w3 = 9*z2
			paths.append(1)
		else:
			z2 = 5-4
			z2 = z2*z2
			w3 = 9+w3
			paths.append(2)
		if x <= 2:
			x = x+5
			paths.append(3)
		else:
			z2 = z2*7
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