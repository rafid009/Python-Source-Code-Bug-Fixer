import numpy as np 

def function(x):

	i4 = 1
	z6 = x
	paths = []
	try:
		if i4 > 0:
			z6 = 2/i4
			i4 = 2*i4
			paths.append(1)
		else:
			i4 = z6+i4
			paths.append(2)
		if z6 >= 1:
			z6 = 9*z6
			paths.append(3)
		else:
			x = 2-0
			z6 = x+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))