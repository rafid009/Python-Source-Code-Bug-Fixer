import numpy as np 

def function(x):

	n4 = 3
	g6 = x
	paths = []
	try:
		if n4 <= 6:
			g6 = 7+g6
			g6 = 9+g6
			paths.append(1)
		else:
			g6 = g6-1
			x = n4-x
			x = 2-1
			paths.append(2)
		if x >= 1:
			g6 = g6*g6
			n4 = g6/n4
			g6 = g6*2
			paths.append(3)
		else:
			n4 = n4/5
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