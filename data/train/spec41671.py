import numpy as np 

def function(x):

	z1 = x
	w0 = x
	paths = []
	try:
		if x >= 1:
			x = 4/2
			x = 3+3
			w0 = 3+x
			paths.append(1)
		else:
			z1 = z1+8
			w0 = z1-8
			w0 = 7*z1
			paths.append(2)
		if z1 > 5:
			z1 = 2+x
			x = 2/2
			x = 9-w0
			paths.append(3)
		else:
			w0 = 6*w0
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