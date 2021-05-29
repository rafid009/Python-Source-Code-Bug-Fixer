import numpy as np 

def function(x):

	g4 = 3
	m4 = x
	x = x
	paths = []
	try:
		if x <= 9:
			g4 = 9+g4
			x = 9*x
			paths.append(1)
		else:
			x = x-g4
			m4 = 0/m4
			m4 = 1/6
			paths.append(2)
		if m4 >= 1:
			x = m4+x
			paths.append(3)
		else:
			x = x+7
			m4 = g4+x
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		g4 = m4**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))