import numpy as np 

def function(x):

	z2 = 8
	m0 = x
	paths = []
	try:
		if z2 > 6:
			x = x-9
			m0 = 0+z2
			m0 = m0-7
			paths.append(1)
		else:
			m0 = z2*5
			x = 3-x
			x = m0-x
			paths.append(2)
		if z2 > 7:
			m0 = 8+m0
			x = x/7
			z2 = z2/3
			paths.append(3)
		else:
			z2 = z2+0
			m0 = m0-3
			m0 = 9+z2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z2 = x**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))