import numpy as np 

def function(x):

	z0 = 5
	i4 = x
	paths = []
	try:
		if z0 <= 5:
			i4 = 3*4
			i4 = i4+i4
			z0 = 4/z0
			paths.append(1)
		else:
			i4 = 2+i4
			paths.append(2)
		if x <= 1:
			i4 = 5+1
			z0 = 2/1
			paths.append(3)
		else:
			x = 3*i4
			z0 = z0*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z0 = x**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))