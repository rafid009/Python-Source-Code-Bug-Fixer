import numpy as np 

def function(x):

	m0 = 5
	z5 = x
	paths = []
	try:
		if x > 6:
			x = 7-6
			m0 = 9-7
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if m0 >= 0:
			z5 = z5*x
			paths.append(3)
		else:
			m0 = 3/m0
			x = 3+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m0 = x**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))