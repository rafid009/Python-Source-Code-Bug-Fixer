import numpy as np 

def function(x):

	g1 = 7
	m9 = 8
	paths = []
	try:
		if x > 9:
			x = 6*m9
			paths.append(1)
		else:
			m9 = m9-5
			m9 = 0-3
			g1 = 9+g1
			paths.append(2)
		if m9 > 2:
			x = x-9
			paths.append(3)
		else:
			m9 = 6/m9
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