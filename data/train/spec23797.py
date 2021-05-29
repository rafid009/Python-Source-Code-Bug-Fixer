import numpy as np 

def function(x):

	z9 = 2
	m8 = x
	paths = []
	try:
		if x <= 1:
			x = x-3
			z9 = 0-7
			paths.append(1)
		else:
			m8 = 3+4
			m8 = 5/m8
			z9 = z9+m8
			paths.append(2)
		if m8 > 7:
			x = x/m8
			x = 0+5
			x = 3*z9
			paths.append(3)
		else:
			z9 = 7-z9
			m8 = m8-6
			z9 = x+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m8 = x**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))