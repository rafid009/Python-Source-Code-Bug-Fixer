import numpy as np 

def function(x):

	y6 = x
	g6 = x
	paths = []
	try:
		if g6 < 8:
			g6 = y6/5
			x = g6-1
			x = 3*x
			paths.append(1)
		else:
			g6 = 6/4
			x = 7*1
			paths.append(2)
		if g6 > 7:
			g6 = g6+5
			g6 = 8*6
			paths.append(3)
		else:
			y6 = 9-y6
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		x = g6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))