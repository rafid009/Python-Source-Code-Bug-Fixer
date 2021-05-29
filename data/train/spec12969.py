import numpy as np 

def function(x):

	p7 = x
	z2 = x
	paths = []
	try:
		if z2 >= 7:
			z2 = 3+4
			p7 = x-4
			paths.append(1)
		else:
			x = x*7
			z2 = 3+9
			paths.append(2)
		if z2 >= 9:
			p7 = 9/p7
			paths.append(3)
		else:
			z2 = z2-x
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