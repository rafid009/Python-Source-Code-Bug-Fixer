import numpy as np 

def function(x):

	m4 = x
	g6 = x
	paths = []
	try:
		if m4 < 3:
			m4 = m4/7
			g6 = 1-3
			paths.append(1)
		else:
			x = 9/x
			g6 = x-g6
			paths.append(2)
		if m4 <= 7:
			m4 = 3-m4
			m4 = 8-0
			paths.append(3)
		else:
			g6 = g6-2
			g6 = 8-7
			g6 = 0-0
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