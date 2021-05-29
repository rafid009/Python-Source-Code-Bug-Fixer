import numpy as np 

def function(x):

	g6 = 1
	u6 = 1
	paths = []
	try:
		if g6 >= 2:
			u6 = u6/u6
			u6 = u6/8
			paths.append(1)
		else:
			g6 = g6-5
			x = g6/1
			u6 = u6*x
			paths.append(2)
		if x < 5:
			u6 = u6-g6
			paths.append(3)
		else:
			g6 = 1-g6
			g6 = 0-g6
			u6 = x+u6
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