import numpy as np 

def function(x):

	g6 = 1
	o4 = 2
	paths = []
	try:
		if g6 < 0:
			o4 = 5+1
			paths.append(1)
		else:
			x = o4/g6
			g6 = 0-1
			o4 = o4+6
			paths.append(2)
		if g6 < 3:
			x = x/o4
			x = o4/x
			paths.append(3)
		else:
			o4 = 6+7
			g6 = g6*0
			g6 = g6*7
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