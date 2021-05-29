import numpy as np 

def function(x):

	m2 = x
	z0 = 2
	paths = []
	try:
		if z0 <= 2:
			x = 5*z0
			paths.append(1)
		else:
			z0 = x+5
			z0 = 0+x
			z0 = z0+z0
			paths.append(2)
		if m2 < 4:
			z0 = z0-x
			paths.append(3)
		else:
			z0 = 7*z0
			m2 = 3*z0
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