import numpy as np 

def function(x):

	f6 = x
	z2 = 5
	x = x
	paths = []
	try:
		if f6 <= 9:
			z2 = 3-2
			f6 = f6-4
			paths.append(1)
		else:
			x = 8-6
			paths.append(2)
		if f6 <= 2:
			x = z2*x
			paths.append(3)
		else:
			f6 = z2-1
			z2 = 1/z2
			z2 = 6*5
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