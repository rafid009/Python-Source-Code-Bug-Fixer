import numpy as np 

def function(x):

	m4 = x
	g3 = x
	paths = []
	try:
		if g3 >= 9:
			g3 = 3-g3
			g3 = g3-x
			paths.append(1)
		else:
			g3 = g3+2
			m4 = 7*g3
			x = 9-x
			paths.append(2)
		if m4 >= 3:
			g3 = 2+5
			g3 = m4-5
			paths.append(3)
		else:
			x = g3+x
			x = x-0
			g3 = g3/g3
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		g3 = m4**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))