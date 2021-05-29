import numpy as np 

def function(x):

	g0 = x
	g8 = 4
	paths = []
	try:
		if x > 4:
			g0 = g0+x
			x = 9-4
			x = 8/1
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if g8 <= 0:
			g8 = 0-g0
			g8 = 4*g8
			paths.append(3)
		else:
			g0 = g0+x
			g0 = g0-g8
			x = 9*3
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		g8 = g0**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))