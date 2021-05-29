import numpy as np 

def function(x):

	z0 = 9
	l2 = 8
	paths = []
	try:
		if l2 > 9:
			x = x-5
			l2 = l2*2
			paths.append(1)
		else:
			z0 = 7/z0
			l2 = l2+l2
			z0 = 0+z0
			paths.append(2)
		if z0 <= 8:
			z0 = 4-7
			paths.append(3)
		else:
			z0 = z0/z0
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		x = z0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))