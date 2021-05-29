import numpy as np 

def function(x):

	m1 = 6
	g4 = 8
	paths = []
	try:
		if x <= 2:
			x = x/x
			paths.append(1)
		else:
			g4 = 5*6
			m1 = 7+0
			x = 8-x
			paths.append(2)
		if x <= 0:
			m1 = m1-g4
			m1 = 1-m1
			paths.append(3)
		else:
			m1 = g4+m1
			g4 = g4*8
			m1 = 8-m1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m1 = x**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))