import numpy as np 

def function(x):

	z3 = x
	m9 = 4
	paths = []
	try:
		if z3 >= 4:
			x = x*z3
			paths.append(1)
		else:
			m9 = z3-2
			paths.append(2)
		if m9 <= 2:
			z3 = z3-3
			m9 = m9-1
			paths.append(3)
		else:
			m9 = z3*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m9 = x**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))