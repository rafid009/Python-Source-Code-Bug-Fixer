import numpy as np 

def function(x):

	y1 = 8
	g3 = x
	paths = []
	try:
		if y1 > 0:
			g3 = 8*x
			paths.append(1)
		else:
			x = x+2
			y1 = y1/7
			x = x+6
			paths.append(2)
		if y1 >= 6:
			g3 = g3-5
			paths.append(3)
		else:
			g3 = 9/x
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