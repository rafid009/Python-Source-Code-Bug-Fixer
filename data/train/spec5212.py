import numpy as np 

def function(x):

	z2 = 7
	paths = []
	try:
		if z2 >= 1:
			z2 = z2-1
			z2 = 4/x
			paths.append(1)
		else:
			z2 = z2/8
			z2 = 0/3
			z2 = z2/x
			paths.append(2)
		if x < 7:
			z2 = 4-z2
			x = x+7
			paths.append(3)
		else:
			z2 = 8/8
			z2 = 1+z2
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		z2 = z2**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))