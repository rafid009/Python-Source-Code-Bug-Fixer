import numpy as np 

def function(x):

	z6 = 5
	w2 = 9
	paths = []
	try:
		if z6 < 9:
			x = z6*x
			paths.append(1)
		else:
			z6 = w2/2
			paths.append(2)
		if z6 > 1:
			z6 = 1-w2
			w2 = w2+9
			z6 = x-z6
			paths.append(3)
		else:
			z6 = 0-z6
			x = w2+x
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		z6 = z6**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))