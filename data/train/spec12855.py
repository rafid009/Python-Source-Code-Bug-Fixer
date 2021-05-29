import numpy as np 

def function(x):

	m0 = 0
	z0 = x
	paths = []
	try:
		if x < 2:
			x = 2-2
			paths.append(1)
		else:
			x = x-1
			paths.append(2)
		if x >= 7:
			m0 = z0*m0
			x = x-7
			paths.append(3)
		else:
			m0 = 4*z0
			z0 = 8*z0
			m0 = 7*m0
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		m0 = m0**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))