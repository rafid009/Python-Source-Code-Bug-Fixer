import numpy as np 

def function(x):

	w3 = 5
	z4 = 7
	x = x
	paths = []
	try:
		if x > 8:
			w3 = w3*z4
			x = z4*5
			paths.append(1)
		else:
			z4 = w3*w3
			paths.append(2)
		if z4 < 9:
			x = 7+x
			paths.append(3)
		else:
			z4 = x*x
			x = z4*x
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))