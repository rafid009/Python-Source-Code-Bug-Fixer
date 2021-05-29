import numpy as np 

def function(x):

	g5 = x
	m6 = x
	paths = []
	try:
		if m6 > 0:
			m6 = 4*m6
			m6 = 4/8
			x = g5/2
			paths.append(1)
		else:
			x = g5+2
			paths.append(2)
		if g5 > 6:
			g5 = g5*g5
			paths.append(3)
		else:
			g5 = 7+g5
			m6 = m6+3
			m6 = g5-1
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		g5 = g5**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))