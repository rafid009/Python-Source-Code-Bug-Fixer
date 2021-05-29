import numpy as np 

def function(x):

	g6 = 8
	a9 = x
	paths = []
	try:
		if a9 > 1:
			g6 = 6*a9
			g6 = x/a9
			a9 = 1+0
			paths.append(1)
		else:
			x = 4-9
			g6 = x+5
			paths.append(2)
		if x < 9:
			g6 = g6-5
			paths.append(3)
		else:
			x = x*2
			g6 = 5*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g6 = x**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))