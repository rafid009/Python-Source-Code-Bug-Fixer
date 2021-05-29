import numpy as np 

def function(x):

	m0 = x
	g7 = x
	paths = []
	try:
		if x >= 8:
			g7 = 4*g7
			x = 3+x
			paths.append(1)
		else:
			g7 = g7+1
			paths.append(2)
		if m0 >= 3:
			x = 9-9
			x = x*m0
			x = g7+4
			paths.append(3)
		else:
			m0 = 9*x
			x = x*3
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		m0 = g7**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))