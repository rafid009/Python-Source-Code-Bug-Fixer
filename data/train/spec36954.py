import numpy as np 

def function(x):

	z6 = 8
	m2 = 3
	paths = []
	try:
		if m2 > 5:
			z6 = z6-m2
			z6 = 7/z6
			z6 = 5*x
			paths.append(1)
		else:
			x = 4-m2
			paths.append(2)
		if z6 > 8:
			m2 = m2/6
			z6 = z6-2
			paths.append(3)
		else:
			z6 = x/z6
			m2 = 3-9
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		z6 = m2**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))