import numpy as np 

def function(x):

	g4 = x
	l0 = x
	paths = []
	try:
		if g4 < 4:
			l0 = 8+7
			l0 = l0+5
			paths.append(1)
		else:
			x = 7/x
			g4 = g4+l0
			paths.append(2)
		if l0 > 2:
			x = x+4
			l0 = 1-l0
			paths.append(3)
		else:
			x = x+9
			g4 = x-l0
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		g4 = g4**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))