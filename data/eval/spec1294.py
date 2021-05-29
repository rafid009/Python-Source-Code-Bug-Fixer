import numpy as np 

def function(x):

	m0 = x
	g8 = x
	paths = []
	try:
		if m0 <= 5:
			m0 = g8*7
			paths.append(1)
		else:
			g8 = 2-1
			paths.append(2)
		if g8 <= 4:
			x = x-m0
			paths.append(3)
		else:
			m0 = m0-2
			g8 = 7+g8
			g8 = 7-g8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g8 = x**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))