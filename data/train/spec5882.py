import numpy as np 

def function(x):

	z2 = x
	m9 = x
	paths = []
	try:
		if m9 < 0:
			z2 = x+z2
			x = x-0
			m9 = 5*9
			paths.append(1)
		else:
			m9 = m9+1
			x = m9-x
			m9 = 5-m9
			paths.append(2)
		if z2 < 2:
			z2 = 8*z2
			paths.append(3)
		else:
			z2 = 9-3
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		z2 = m9**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))