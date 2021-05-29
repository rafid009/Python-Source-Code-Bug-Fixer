import numpy as np 

def function(x):

	g3 = 1
	l0 = x
	paths = []
	try:
		if g3 < 3:
			g3 = g3-1
			paths.append(1)
		else:
			x = x-8
			l0 = l0*9
			g3 = 9*7
			paths.append(2)
		if l0 >= 2:
			l0 = 8/x
			g3 = g3-x
			paths.append(3)
		else:
			l0 = l0-3
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		g3 = g3**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))