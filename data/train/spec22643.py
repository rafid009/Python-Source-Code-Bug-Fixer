import numpy as np 

def function(x):

	m0 = x
	g7 = 4
	paths = []
	try:
		if x > 6:
			g7 = 2*g7
			paths.append(1)
		else:
			g7 = 3/g7
			m0 = 6*x
			paths.append(2)
		if m0 < 4:
			m0 = m0+1
			g7 = g7+g7
			m0 = m0+m0
			paths.append(3)
		else:
			m0 = m0-m0
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		g7 = m0**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))