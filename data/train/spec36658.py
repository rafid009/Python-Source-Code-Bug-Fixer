import numpy as np 

def function(x):

	z3 = 2
	m6 = x
	paths = []
	try:
		if x < 9:
			m6 = 3-2
			m6 = m6*x
			x = 4*x
			paths.append(1)
		else:
			z3 = z3/3
			x = x+z3
			paths.append(2)
		if x >= 9:
			z3 = z3/1
			paths.append(3)
		else:
			m6 = m6+9
			x = m6-6
			m6 = m6*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))