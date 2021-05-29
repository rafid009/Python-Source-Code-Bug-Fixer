import numpy as np 

def function(x):

	m6 = 3
	g3 = x
	paths = []
	try:
		if g3 >= 7:
			g3 = g3+9
			g3 = g3*8
			paths.append(1)
		else:
			m6 = x*g3
			m6 = m6*m6
			paths.append(2)
		if g3 > 6:
			x = 9-x
			m6 = m6+9
			x = 0-0
			paths.append(3)
		else:
			m6 = x+m6
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		g3 = m6**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))