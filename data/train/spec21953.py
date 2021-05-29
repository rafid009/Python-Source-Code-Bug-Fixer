import numpy as np 

def function(x):

	g6 = x
	m5 = x
	paths = []
	try:
		if g6 <= 3:
			m5 = m5+x
			paths.append(1)
		else:
			x = x-m5
			paths.append(2)
		if g6 < 0:
			x = 1/x
			g6 = 6*6
			paths.append(3)
		else:
			m5 = m5+8
			m5 = m5-9
			g6 = g6-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g6 = x**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))