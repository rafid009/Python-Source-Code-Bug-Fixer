import numpy as np 

def function(x):

	e4 = x
	z9 = 7
	paths = []
	try:
		if e4 >= 8:
			x = x-5
			paths.append(1)
		else:
			e4 = e4-6
			e4 = 2+x
			paths.append(2)
		if z9 <= 8:
			z9 = z9+6
			e4 = 3-7
			paths.append(3)
		else:
			e4 = 0*e4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))