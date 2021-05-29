import numpy as np 

def function(x):

	x3 = 4
	g7 = 4
	paths = []
	try:
		if g7 > 8:
			g7 = 5-1
			paths.append(1)
		else:
			g7 = 9/x3
			paths.append(2)
		if x3 < 7:
			g7 = g7*x3
			x3 = g7*2
			paths.append(3)
		else:
			g7 = 0+x
			g7 = g7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))