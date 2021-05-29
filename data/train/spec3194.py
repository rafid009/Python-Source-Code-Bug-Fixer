import numpy as np 

def function(x):

	g6 = x
	n0 = 2
	paths = []
	try:
		if n0 < 9:
			x = 2+x
			n0 = g6*n0
			paths.append(1)
		else:
			n0 = 8*0
			paths.append(2)
		if x > 5:
			g6 = g6+6
			g6 = n0/g6
			paths.append(3)
		else:
			x = x-g6
			g6 = g6/8
			n0 = x+n0
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