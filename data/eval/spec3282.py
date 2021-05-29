import numpy as np 

def function(x):

	w0 = 0
	z6 = 8
	paths = []
	try:
		if x >= 5:
			w0 = 0+w0
			paths.append(1)
		else:
			z6 = 4-z6
			x = x+2
			paths.append(2)
		if x > 2:
			x = x-5
			paths.append(3)
		else:
			z6 = w0-z6
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		x = z6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))