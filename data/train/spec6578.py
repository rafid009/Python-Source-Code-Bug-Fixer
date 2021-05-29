import numpy as np 

def function(x):

	g6 = 2
	g5 = x
	x = x
	paths = []
	try:
		if g6 > 2:
			g6 = g6*g6
			g5 = 7+g5
			x = 3-x
			paths.append(1)
		else:
			g5 = g6+g5
			paths.append(2)
		if g5 < 9:
			x = x+1
			g6 = 1/g6
			paths.append(3)
		else:
			g5 = g5+2
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		g6 = g5**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))