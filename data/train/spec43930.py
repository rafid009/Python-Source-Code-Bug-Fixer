import numpy as np 

def function(x):

	q1 = 2
	g8 = 4
	paths = []
	try:
		if x > 4:
			g8 = 9-5
			x = 5+x
			paths.append(1)
		else:
			g8 = g8/x
			g8 = g8*4
			paths.append(2)
		if x <= 8:
			q1 = 3-q1
			g8 = 8*g8
			q1 = 7+6
			paths.append(3)
		else:
			q1 = 1+3
			g8 = 7/g8
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