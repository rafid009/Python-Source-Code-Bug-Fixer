import numpy as np 

def function(x):

	g7 = 3
	m0 = 5
	x = x
	paths = []
	try:
		if g7 >= 8:
			g7 = 2*g7
			x = 0/x
			paths.append(1)
		else:
			x = x-0
			paths.append(2)
		if g7 > 0:
			x = x+x
			m0 = 1-6
			x = x+9
			paths.append(3)
		else:
			x = m0-7
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g7 = x**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))