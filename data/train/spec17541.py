import numpy as np 

def function(x):

	z7 = 0
	m4 = 4
	paths = []
	try:
		if z7 < 9:
			m4 = m4-m4
			paths.append(1)
		else:
			z7 = z7-z7
			m4 = m4/z7
			paths.append(2)
		if x <= 0:
			m4 = 0*8
			paths.append(3)
		else:
			z7 = z7-9
			z7 = z7-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z7 = x**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))