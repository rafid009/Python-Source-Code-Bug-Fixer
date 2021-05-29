import numpy as np 

def function(x):

	z3 = 4
	m2 = x
	paths = []
	try:
		if m2 < 6:
			z3 = z3+x
			z3 = x-z3
			z3 = 4+z3
			paths.append(1)
		else:
			m2 = 5/m2
			paths.append(2)
		if z3 < 4:
			m2 = 8+m2
			paths.append(3)
		else:
			x = x-2
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		m2 = m2**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))