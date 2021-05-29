import numpy as np 

def function(x):

	z2 = x
	i0 = x
	paths = []
	try:
		if z2 <= 3:
			z2 = 4*z2
			i0 = 9*i0
			paths.append(1)
		else:
			x = i0/x
			z2 = z2+5
			paths.append(2)
		if x < 9:
			z2 = z2+5
			i0 = 3+i0
			x = x+z2
			paths.append(3)
		else:
			x = x-3
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))