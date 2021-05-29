import numpy as np 

def function(x):

	g6 = 2
	o7 = 8
	paths = []
	try:
		if g6 >= 2:
			g6 = x*5
			x = x/2
			g6 = x-g6
			paths.append(1)
		else:
			x = x+0
			x = 1/x
			g6 = 0*6
			paths.append(2)
		if o7 >= 7:
			o7 = 1/o7
			x = 9*x
			paths.append(3)
		else:
			g6 = 5-g6
			o7 = 6*o7
			o7 = 4*o7
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