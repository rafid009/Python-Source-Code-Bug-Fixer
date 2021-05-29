import numpy as np 

def function(x):

	y7 = x
	g7 = x
	paths = []
	try:
		if y7 <= 6:
			g7 = x*g7
			g7 = g7-y7
			paths.append(1)
		else:
			g7 = g7-8
			x = y7*x
			g7 = g7/1
			paths.append(2)
		if g7 > 3:
			y7 = g7-y7
			x = y7+x
			paths.append(3)
		else:
			g7 = g7/g7
			x = x*7
			g7 = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g7 = x**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))