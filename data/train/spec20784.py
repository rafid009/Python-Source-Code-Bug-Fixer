import numpy as np 

def function(x):

	z0 = 8
	m2 = x
	paths = []
	try:
		if z0 < 1:
			x = m2*x
			z0 = z0*0
			paths.append(1)
		else:
			x = x/7
			z0 = 7/z0
			m2 = m2-7
			paths.append(2)
		if z0 > 4:
			z0 = x+z0
			paths.append(3)
		else:
			m2 = m2*5
			m2 = m2/5
			x = z0/6
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		z0 = m2**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))