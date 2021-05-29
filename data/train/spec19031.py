import numpy as np 

def function(x):

	m8 = 3
	z0 = x
	paths = []
	try:
		if x >= 3:
			z0 = m8/x
			paths.append(1)
		else:
			m8 = 4+2
			x = x-6
			paths.append(2)
		if z0 >= 2:
			m8 = z0-m8
			x = x-8
			paths.append(3)
		else:
			x = z0-x
			z0 = z0-m8
			z0 = 8*4
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		x = m8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))