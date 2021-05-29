import numpy as np 

def function(x):

	m7 = x
	z7 = x
	paths = []
	try:
		if z7 < 6:
			z7 = 4/z7
			z7 = 8/3
			x = m7-z7
			paths.append(1)
		else:
			x = x*z7
			z7 = 8*z7
			paths.append(2)
		if m7 <= 8:
			z7 = z7-7
			m7 = m7/6
			z7 = z7*z7
			paths.append(3)
		else:
			x = 1*z7
			z7 = 5/6
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