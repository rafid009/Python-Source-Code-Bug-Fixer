import numpy as np 

def function(x):

	z2 = 6
	f3 = x
	paths = []
	try:
		if f3 >= 0:
			z2 = 1/x
			f3 = f3-7
			z2 = 3+z2
			paths.append(1)
		else:
			z2 = 5/z2
			paths.append(2)
		if f3 <= 1:
			f3 = f3*8
			paths.append(3)
		else:
			x = z2+z2
			x = x-z2
			z2 = 4-z2
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