import numpy as np 

def function(x):

	q4 = x
	g8 = 4
	paths = []
	try:
		if q4 >= 5:
			g8 = q4-g8
			q4 = 6-3
			paths.append(1)
		else:
			g8 = 8+g8
			q4 = q4-9
			paths.append(2)
		if g8 < 0:
			q4 = 4/7
			g8 = 0*g8
			g8 = 4-g8
			paths.append(3)
		else:
			g8 = g8*8
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