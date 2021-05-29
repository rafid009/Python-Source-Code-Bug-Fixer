import numpy as np 

def function(x):

	m8 = 3
	g6 = x
	paths = []
	try:
		if x >= 6:
			m8 = g6*m8
			paths.append(1)
		else:
			g6 = g6/6
			m8 = m8/5
			g6 = 7+3
			paths.append(2)
		if x <= 7:
			m8 = m8-m8
			x = x-2
			m8 = m8-9
			paths.append(3)
		else:
			x = x/g6
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		g6 = m8**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))