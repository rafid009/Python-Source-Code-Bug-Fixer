import numpy as np 

def function(x):

	g4 = x
	e9 = 9
	paths = []
	try:
		if e9 < 6:
			g4 = g4-3
			paths.append(1)
		else:
			e9 = 1-5
			x = 2+6
			x = 3/x
			paths.append(2)
		if g4 > 5:
			e9 = 1*7
			paths.append(3)
		else:
			x = x/x
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