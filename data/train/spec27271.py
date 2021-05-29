import numpy as np 

def function(x):

	g7 = 1
	u6 = x
	paths = []
	try:
		if g7 < 2:
			g7 = 1/5
			paths.append(1)
		else:
			g7 = x/g7
			paths.append(2)
		if u6 >= 5:
			g7 = 6-x
			g7 = 5/7
			g7 = g7*g7
			paths.append(3)
		else:
			g7 = 6*g7
			g7 = u6-7
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		g7 = g7**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))