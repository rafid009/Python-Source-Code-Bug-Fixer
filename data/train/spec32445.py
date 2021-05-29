import numpy as np 

def function(x):

	m8 = 4
	z1 = x
	paths = []
	try:
		if x < 5:
			m8 = 9*m8
			m8 = m8-1
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if m8 > 5:
			x = 1-2
			m8 = m8+z1
			paths.append(3)
		else:
			m8 = m8-9
			z1 = z1/5
			x = m8*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))