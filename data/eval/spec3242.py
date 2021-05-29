import numpy as np 

def function(x):

	z5 = 8
	m8 = x
	paths = []
	try:
		if x <= 1:
			x = 7-x
			m8 = 5+m8
			paths.append(1)
		else:
			z5 = z5/x
			x = z5-x
			x = 4+x
			paths.append(2)
		if m8 >= 6:
			x = x+m8
			m8 = m8-5
			paths.append(3)
		else:
			x = m8/9
			m8 = 4/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z5 = x**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))