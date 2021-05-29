import numpy as np 

def function(x):

	g8 = 5
	q9 = 6
	paths = []
	try:
		if q9 > 1:
			q9 = 3/q9
			q9 = q9+x
			paths.append(1)
		else:
			x = x+8
			g8 = g8*q9
			g8 = x+0
			paths.append(2)
		if x <= 6:
			g8 = q9*q9
			paths.append(3)
		else:
			q9 = q9*g8
			g8 = 9/g8
			q9 = x/q9
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