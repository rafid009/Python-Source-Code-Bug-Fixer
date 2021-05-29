import numpy as np 

def function(x):

	g4 = x
	e5 = x
	paths = []
	try:
		if x < 2:
			g4 = e5+1
			paths.append(1)
		else:
			g4 = e5-g4
			paths.append(2)
		if e5 <= 5:
			e5 = e5+4
			x = g4*4
			paths.append(3)
		else:
			g4 = x+4
			g4 = g4-g4
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