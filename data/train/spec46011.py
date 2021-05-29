import numpy as np 

def function(x):

	z7 = 8
	m6 = 4
	paths = []
	try:
		if x < 4:
			x = z7+m6
			x = z7*x
			paths.append(1)
		else:
			z7 = z7-2
			x = z7-x
			m6 = 1-2
			paths.append(2)
		if x < 6:
			z7 = 1-x
			z7 = m6*5
			paths.append(3)
		else:
			x = 3+x
			m6 = m6*z7
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		x = m6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))