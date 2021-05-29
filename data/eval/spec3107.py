import numpy as np 

def function(x):

	x8 = 3
	g4 = x
	paths = []
	try:
		if x8 >= 0:
			x = 6*x
			x8 = x8-3
			paths.append(1)
		else:
			x8 = 3*9
			x8 = x8+x8
			x = x+2
			paths.append(2)
		if g4 >= 3:
			g4 = 5*g4
			x = x-x8
			g4 = x8/8
			paths.append(3)
		else:
			x = x8+x
			g4 = g4/4
			x8 = x8*x8
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