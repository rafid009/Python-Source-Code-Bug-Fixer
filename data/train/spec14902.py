import numpy as np 

def function(x):

	m6 = x
	g7 = 9
	paths = []
	try:
		if g7 < 0:
			m6 = m6/m6
			x = 0-x
			g7 = 8/g7
			paths.append(1)
		else:
			g7 = g7-0
			m6 = 3-m6
			paths.append(2)
		if m6 >= 4:
			g7 = g7/5
			paths.append(3)
		else:
			m6 = m6*7
			g7 = x*9
			m6 = m6*7
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		g7 = g7**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))