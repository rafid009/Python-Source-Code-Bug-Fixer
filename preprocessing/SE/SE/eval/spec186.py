import numpy as np 

def function(x):

	g7 = 4
	g4 = x
	paths = []
	try:
		if g7 >= 8:
			g7 = 9/g7
			paths.append(1)
		else:
			g4 = g4*3
			x = 5+x
			paths.append(2)
		if g4 > 3:
			x = g7-x
			g7 = 5*g4
			paths.append(3)
		else:
			g7 = x*3
			g7 = x-g7
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		x = g4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))