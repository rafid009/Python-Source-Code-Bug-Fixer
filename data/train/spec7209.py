import numpy as np 

def function(x):

	m4 = 1
	z5 = 5
	paths = []
	try:
		if z5 < 0:
			m4 = 9+m4
			z5 = z5*0
			paths.append(1)
		else:
			z5 = z5*x
			paths.append(2)
		if m4 > 3:
			x = 9*1
			paths.append(3)
		else:
			z5 = 6/7
			m4 = m4-7
			z5 = z5-x
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		m4 = m4**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))