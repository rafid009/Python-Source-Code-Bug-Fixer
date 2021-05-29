import numpy as np 

def function(x):

	g5 = x
	g0 = x
	paths = []
	try:
		if g5 >= 8:
			g0 = 9*g0
			paths.append(1)
		else:
			g0 = 9+g0
			g5 = 5-g5
			g5 = 6+x
			paths.append(2)
		if g5 > 8:
			g0 = 7+g0
			paths.append(3)
		else:
			g5 = 0-5
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		g5 = g0**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))