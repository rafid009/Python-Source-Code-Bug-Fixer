import numpy as np 

def function(x):

	w6 = 6
	g6 = x
	paths = []
	try:
		if x > 8:
			g6 = w6+x
			g6 = 0+w6
			paths.append(1)
		else:
			x = x/g6
			paths.append(2)
		if x < 9:
			g6 = w6/5
			paths.append(3)
		else:
			g6 = 9/g6
			g6 = 2-7
			x = g6*x
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