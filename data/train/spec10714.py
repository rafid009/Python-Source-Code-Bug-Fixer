import numpy as np 

def function(x):

	z9 = x
	m6 = x
	paths = []
	try:
		if z9 >= 5:
			m6 = m6*8
			m6 = m6-6
			paths.append(1)
		else:
			z9 = z9*2
			x = x-2
			z9 = 8+2
			paths.append(2)
		if z9 >= 4:
			m6 = m6/x
			paths.append(3)
		else:
			m6 = 7+2
			z9 = z9-3
			m6 = m6-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))