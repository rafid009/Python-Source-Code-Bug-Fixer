import numpy as np 

def function(x):

	m8 = 6
	z6 = 9
	paths = []
	try:
		if m8 <= 4:
			m8 = z6-m8
			m8 = m8+x
			paths.append(1)
		else:
			z6 = 5/m8
			paths.append(2)
		if m8 > 0:
			z6 = z6+0
			m8 = m8+z6
			m8 = 0*5
			paths.append(3)
		else:
			m8 = m8/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))