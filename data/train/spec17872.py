import numpy as np 

def function(x):

	m0 = 6
	g7 = x
	x = 8
	paths = []
	try:
		if g7 < 5:
			x = 1*x
			paths.append(1)
		else:
			m0 = 4-m0
			m0 = m0-7
			x = 0*7
			paths.append(2)
		if g7 >= 1:
			m0 = 0-x
			x = x-x
			paths.append(3)
		else:
			g7 = g7+g7
			g7 = g7*5
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		x = g7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))