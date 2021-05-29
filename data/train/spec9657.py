import numpy as np 

def function(x):

	o4 = x
	g6 = x
	paths = []
	try:
		if o4 < 5:
			o4 = o4-x
			x = 6/x
			g6 = o4-g6
			paths.append(1)
		else:
			g6 = 1*g6
			paths.append(2)
		if x >= 3:
			g6 = g6-8
			paths.append(3)
		else:
			g6 = g6-7
			o4 = o4*o4
			x = 4+1
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