import numpy as np 

def function(x):

	g4 = 8
	a8 = x
	paths = []
	try:
		if x < 3:
			g4 = x*g4
			paths.append(1)
		else:
			g4 = a8-a8
			g4 = 0*g4
			paths.append(2)
		if x < 9:
			a8 = a8-3
			paths.append(3)
		else:
			a8 = 8+8
			g4 = a8+g4
			x = g4+0
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