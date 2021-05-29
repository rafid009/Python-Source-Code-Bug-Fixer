import numpy as np 

def function(x):

	m2 = x
	z2 = x
	x = x
	paths = []
	try:
		if m2 <= 1:
			m2 = 4*m2
			m2 = 6/7
			paths.append(1)
		else:
			z2 = 2-7
			z2 = 9/z2
			paths.append(2)
		if m2 < 1:
			z2 = 9-m2
			z2 = z2+7
			z2 = x/2
			paths.append(3)
		else:
			z2 = z2*6
			m2 = 2/m2
			x = 3-z2
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		z2 = z2**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))