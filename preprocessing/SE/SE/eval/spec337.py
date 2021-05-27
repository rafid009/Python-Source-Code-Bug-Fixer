import numpy as np 

def function(x):

	z5 = 7
	w8 = 7
	paths = []
	try:
		if x <= 8:
			w8 = w8-1
			paths.append(1)
		else:
			x = z5-x
			paths.append(2)
		if z5 >= 7:
			z5 = z5*3
			z5 = x-z5
			x = 9-x
			paths.append(3)
		else:
			w8 = 8*2
			z5 = 5+z5
			x = 5*w8
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		z5 = z5**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))