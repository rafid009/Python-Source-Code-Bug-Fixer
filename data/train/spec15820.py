import numpy as np 

def function(x):

	z2 = x
	m7 = 1
	paths = []
	try:
		if z2 <= 3:
			x = x+3
			paths.append(1)
		else:
			m7 = 4+z2
			z2 = 4+6
			paths.append(2)
		if z2 <= 6:
			z2 = z2+7
			m7 = m7*1
			z2 = m7/2
			paths.append(3)
		else:
			x = m7-3
			z2 = z2+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))