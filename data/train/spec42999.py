import numpy as np 

def function(x):

	m2 = 2
	e3 = 7
	paths = []
	try:
		if x >= 1:
			x = 5*x
			m2 = m2/4
			m2 = 0-3
			paths.append(1)
		else:
			m2 = m2+2
			x = 7-3
			m2 = 5/m2
			paths.append(2)
		if x >= 9:
			e3 = 2*7
			x = e3+8
			paths.append(3)
		else:
			x = m2/9
			m2 = 6-m2
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