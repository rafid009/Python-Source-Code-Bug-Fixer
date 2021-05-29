import numpy as np 

def function(x):

	z2 = 9
	w9 = 5
	paths = []
	try:
		if z2 >= 0:
			z2 = 4/w9
			z2 = z2/3
			paths.append(1)
		else:
			z2 = z2-x
			paths.append(2)
		if x < 4:
			w9 = w9-7
			x = w9-z2
			paths.append(3)
		else:
			x = x*4
			w9 = z2+w9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z2 = x**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))