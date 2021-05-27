import numpy as np 

def function(x):

	z3 = x
	m9 = 7
	paths = []
	try:
		if x >= 8:
			z3 = x-m9
			m9 = x*m9
			paths.append(1)
		else:
			x = m9-z3
			z3 = m9*z3
			z3 = z3*2
			paths.append(2)
		if m9 > 5:
			m9 = 5+9
			z3 = 5/5
			z3 = 2+1
			paths.append(3)
		else:
			x = x*5
			x = x+z3
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