import numpy as np 

def function(x):

	z6 = x
	m8 = x
	x = 9
	paths = []
	try:
		if m8 >= 7:
			m8 = 0/z6
			x = z6/6
			paths.append(1)
		else:
			m8 = x-9
			paths.append(2)
		if m8 < 7:
			x = x-3
			z6 = z6*x
			m8 = 0/x
			paths.append(3)
		else:
			m8 = m8*x
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		m8 = z6**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))