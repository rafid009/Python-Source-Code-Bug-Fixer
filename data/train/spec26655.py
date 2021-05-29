import numpy as np 

def function(x):

	g9 = 4
	v5 = 1
	paths = []
	try:
		if v5 < 1:
			x = 0/7
			paths.append(1)
		else:
			g9 = g9*3
			g9 = 9/g9
			g9 = 7/4
			paths.append(2)
		if v5 > 5:
			g9 = g9-3
			g9 = g9-1
			g9 = 0-v5
			paths.append(3)
		else:
			g9 = 6*g9
			g9 = 0*g9
			x = v5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g9 = x**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))