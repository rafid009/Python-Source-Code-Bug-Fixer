import numpy as np 

def function(x):

	g3 = 6
	m3 = x
	paths = []
	try:
		if x < 5:
			g3 = g3+3
			paths.append(1)
		else:
			g3 = 5+g3
			paths.append(2)
		if m3 > 0:
			m3 = m3*m3
			g3 = g3+x
			paths.append(3)
		else:
			m3 = m3*8
			g3 = 3*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g3 = x**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))