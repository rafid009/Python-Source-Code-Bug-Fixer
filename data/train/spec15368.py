import numpy as np 

def function(x):

	g4 = x
	m9 = x
	paths = []
	try:
		if x >= 2:
			x = 3+x
			paths.append(1)
		else:
			g4 = g4-1
			g4 = g4-3
			paths.append(2)
		if x <= 7:
			g4 = 7/x
			x = x/x
			x = 2-5
			paths.append(3)
		else:
			m9 = g4*m9
			g4 = x*x
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		m9 = g4**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))