import numpy as np 

def function(x):

	g8 = 3
	q7 = 5
	paths = []
	try:
		if x > 5:
			g8 = 4-g8
			paths.append(1)
		else:
			q7 = x-9
			paths.append(2)
		if q7 >= 8:
			g8 = 3-g8
			x = 6*6
			paths.append(3)
		else:
			g8 = q7/x
			g8 = x*g8
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		g8 = q7**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))