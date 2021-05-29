import numpy as np 

def function(x):

	m9 = 7
	z6 = 1
	paths = []
	try:
		if z6 >= 4:
			z6 = 1+z6
			paths.append(1)
		else:
			x = 1*1
			z6 = 7+x
			z6 = 4-z6
			paths.append(2)
		if z6 <= 2:
			m9 = m9/8
			m9 = m9*x
			m9 = z6-9
			paths.append(3)
		else:
			z6 = 0-z6
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		m9 = z6**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))