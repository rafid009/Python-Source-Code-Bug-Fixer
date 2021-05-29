import numpy as np 

def function(x):

	z8 = 9
	m1 = 1
	paths = []
	try:
		if m1 < 0:
			m1 = m1/8
			m1 = m1/m1
			paths.append(1)
		else:
			m1 = 8+z8
			paths.append(2)
		if x < 3:
			z8 = z8+9
			m1 = 5*m1
			z8 = z8/5
			paths.append(3)
		else:
			x = x-7
			z8 = 6-z8
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		m1 = z8**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))