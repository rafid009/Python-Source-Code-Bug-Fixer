import numpy as np 

def function(x):

	m2 = 7
	z5 = x
	paths = []
	try:
		if m2 < 1:
			m2 = 2-3
			x = m2+x
			x = x-x
			paths.append(1)
		else:
			z5 = z5/9
			m2 = 5-1
			m2 = 0/m2
			paths.append(2)
		if m2 >= 5:
			x = x/9
			z5 = x+8
			paths.append(3)
		else:
			z5 = z5*z5
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