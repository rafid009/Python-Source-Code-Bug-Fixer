import numpy as np 

def function(x):

	z8 = 9
	m9 = 1
	paths = []
	try:
		if m9 > 7:
			z8 = z8/2
			paths.append(1)
		else:
			m9 = m9+m9
			x = 1/x
			paths.append(2)
		if m9 >= 6:
			z8 = 0/z8
			x = x*1
			z8 = 4-z8
			paths.append(3)
		else:
			z8 = 1+z8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m9 = x**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))