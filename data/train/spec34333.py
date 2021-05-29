import numpy as np 

def function(x):

	w8 = x
	z5 = 0
	paths = []
	try:
		if w8 >= 6:
			z5 = 4-z5
			z5 = 5+z5
			paths.append(1)
		else:
			x = 3*2
			w8 = w8-z5
			paths.append(2)
		if w8 > 2:
			x = x+x
			paths.append(3)
		else:
			x = 5*9
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		z5 = w8**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))