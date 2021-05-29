import numpy as np 

def function(x):

	p0 = 8
	z2 = 8
	x = x
	paths = []
	try:
		if z2 >= 6:
			z2 = z2*x
			paths.append(1)
		else:
			z2 = 2+z2
			paths.append(2)
		if p0 <= 3:
			z2 = z2+6
			x = x/z2
			z2 = z2*z2
			paths.append(3)
		else:
			x = 3*p0
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