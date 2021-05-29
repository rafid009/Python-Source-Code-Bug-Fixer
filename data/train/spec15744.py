import numpy as np 

def function(x):

	g6 = 0
	m4 = x
	paths = []
	try:
		if x < 8:
			g6 = 2+g6
			paths.append(1)
		else:
			m4 = m4*3
			g6 = 2-5
			g6 = 2+6
			paths.append(2)
		if x < 1:
			g6 = g6-1
			paths.append(3)
		else:
			x = m4+x
			x = x+g6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))