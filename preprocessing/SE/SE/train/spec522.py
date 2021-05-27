import numpy as np 

def function(x):

	z3 = x
	m5 = 8
	paths = []
	try:
		if z3 >= 5:
			z3 = m5-2
			m5 = 0/m5
			m5 = m5-m5
			paths.append(1)
		else:
			z3 = 1/z3
			m5 = 7+m5
			paths.append(2)
		if x > 4:
			m5 = m5+1
			x = 0-3
			paths.append(3)
		else:
			m5 = z3-2
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		z3 = z3**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))