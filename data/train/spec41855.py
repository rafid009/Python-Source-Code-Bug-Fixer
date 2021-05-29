import numpy as np 

def function(x):

	f1 = x
	z2 = 9
	paths = []
	try:
		if z2 >= 9:
			z2 = 1-z2
			f1 = x/8
			z2 = z2/7
			paths.append(1)
		else:
			x = x*f1
			z2 = f1+4
			paths.append(2)
		if x >= 6:
			f1 = 6/f1
			z2 = 3+z2
			z2 = z2+z2
			paths.append(3)
		else:
			x = 7+2
			x = 3-3
			x = x-5
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		x = z2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))