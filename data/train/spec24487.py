import numpy as np 

def function(x):

	w7 = 7
	z6 = 5
	x = x
	paths = []
	try:
		if z6 >= 0:
			w7 = w7+4
			w7 = 1*0
			z6 = w7/7
			paths.append(1)
		else:
			z6 = w7/3
			paths.append(2)
		if w7 < 2:
			z6 = z6*x
			z6 = 6+z6
			paths.append(3)
		else:
			x = 3/x
			x = z6*x
			w7 = w7+x
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