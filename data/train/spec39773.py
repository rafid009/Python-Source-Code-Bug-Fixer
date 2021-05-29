import numpy as np 

def function(x):

	w2 = 4
	z4 = 8
	paths = []
	try:
		if w2 >= 4:
			z4 = 1*z4
			x = x+z4
			paths.append(1)
		else:
			w2 = 5/2
			x = 6/x
			z4 = 4-w2
			paths.append(2)
		if w2 > 1:
			z4 = z4-9
			w2 = w2/2
			z4 = 5+2
			paths.append(3)
		else:
			x = 4/8
			z4 = 4*z4
			x = 2/x
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