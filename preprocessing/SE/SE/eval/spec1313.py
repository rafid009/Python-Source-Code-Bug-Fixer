import numpy as np 

def function(x):

	i5 = 6
	g7 = x
	paths = []
	try:
		if g7 <= 8:
			g7 = g7-6
			paths.append(1)
		else:
			g7 = x+7
			i5 = 4+3
			i5 = i5+7
			paths.append(2)
		if g7 < 2:
			g7 = x-g7
			paths.append(3)
		else:
			g7 = g7-4
			x = 3/5
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