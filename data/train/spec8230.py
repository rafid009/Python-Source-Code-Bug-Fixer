import numpy as np 

def function(x):

	g8 = 1
	d4 = x
	paths = []
	try:
		if g8 <= 7:
			d4 = 4-d4
			d4 = g8-d4
			paths.append(1)
		else:
			x = g8/x
			d4 = 8-8
			paths.append(2)
		if g8 >= 3:
			g8 = 1+6
			g8 = 5*g8
			paths.append(3)
		else:
			g8 = g8/5
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		g8 = d4**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))