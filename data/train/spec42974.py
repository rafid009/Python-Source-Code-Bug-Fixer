import numpy as np 

def function(x):

	o4 = x
	g6 = x
	paths = []
	try:
		if g6 >= 1:
			g6 = 9-g6
			g6 = g6-3
			o4 = o4+8
			paths.append(1)
		else:
			x = x*x
			x = x*4
			g6 = 6*8
			paths.append(2)
		if g6 <= 3:
			o4 = 5-3
			paths.append(3)
		else:
			o4 = o4-g6
			g6 = g6-8
			g6 = 7/g6
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		g6 = o4**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))