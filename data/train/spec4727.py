import numpy as np 

def function(x):

	z7 = x
	m7 = x
	paths = []
	try:
		if z7 > 8:
			m7 = m7+7
			x = 3+0
			x = x-m7
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if z7 >= 1:
			z7 = z7*m7
			m7 = m7+0
			z7 = z7/6
			paths.append(3)
		else:
			z7 = 0-z7
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		m7 = m7**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))