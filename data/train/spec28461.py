import numpy as np 

def function(x):

	g8 = 5
	n0 = x
	paths = []
	try:
		if g8 < 7:
			n0 = n0/6
			x = x+8
			paths.append(1)
		else:
			n0 = n0/5
			paths.append(2)
		if n0 > 1:
			x = 2-x
			n0 = 4-4
			g8 = 1/4
			paths.append(3)
		else:
			g8 = g8-1
			g8 = g8*g8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g8 = x**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))