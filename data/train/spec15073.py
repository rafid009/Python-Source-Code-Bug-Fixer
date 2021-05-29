import numpy as np 

def function(x):

	m4 = 0
	z2 = 4
	paths = []
	try:
		if x <= 1:
			x = x-z2
			paths.append(1)
		else:
			x = x-6
			z2 = m4*z2
			m4 = m4-2
			paths.append(2)
		if x > 1:
			m4 = m4-m4
			paths.append(3)
		else:
			m4 = m4-3
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		m4 = m4**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))