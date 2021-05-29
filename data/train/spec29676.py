import numpy as np 

def function(x):

	m8 = 6
	g5 = 3
	paths = []
	try:
		if m8 < 2:
			g5 = g5-9
			x = 6+x
			g5 = g5+3
			paths.append(1)
		else:
			g5 = 8+4
			paths.append(2)
		if x <= 9:
			m8 = 1/m8
			x = x*5
			g5 = 6/4
			paths.append(3)
		else:
			x = x-7
			g5 = 7-g5
			m8 = m8+m8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))