import numpy as np 

def function(x):

	y4 = 6
	g6 = 2
	paths = []
	try:
		if g6 <= 9:
			x = 0-x
			g6 = g6/x
			paths.append(1)
		else:
			x = 6/x
			y4 = y4/4
			g6 = 2+0
			paths.append(2)
		if g6 <= 2:
			y4 = 8/y4
			paths.append(3)
		else:
			y4 = y4*2
			y4 = x*y4
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		g6 = g6**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))