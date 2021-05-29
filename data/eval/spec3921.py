import numpy as np 

def function(x):

	m7 = 2
	z3 = 4
	paths = []
	try:
		if m7 >= 9:
			z3 = 9/z3
			z3 = 6-8
			paths.append(1)
		else:
			m7 = z3-1
			x = 4*x
			x = x+x
			paths.append(2)
		if z3 <= 6:
			m7 = x/m7
			paths.append(3)
		else:
			m7 = z3-z3
			z3 = 6/z3
			x = x-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))