import numpy as np 

def function(x):

	z0 = 3
	m2 = x
	paths = []
	try:
		if z0 > 1:
			x = x/3
			z0 = m2/z0
			m2 = 2/x
			paths.append(1)
		else:
			m2 = 2+z0
			paths.append(2)
		if z0 >= 9:
			m2 = 3/m2
			paths.append(3)
		else:
			z0 = 6+z0
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		z0 = z0**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))