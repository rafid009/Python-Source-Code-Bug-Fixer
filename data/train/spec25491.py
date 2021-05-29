import numpy as np 

def function(x):

	m4 = x
	z6 = x
	paths = []
	try:
		if m4 >= 5:
			z6 = z6+7
			z6 = x+x
			m4 = m4-0
			paths.append(1)
		else:
			x = 6-2
			z6 = 7/m4
			paths.append(2)
		if m4 >= 2:
			z6 = z6*9
			paths.append(3)
		else:
			m4 = 5-2
			m4 = 6+8
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		m4 = z6**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))