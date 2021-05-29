import numpy as np 

def function(x):

	g7 = 6
	q3 = x
	paths = []
	try:
		if x > 1:
			q3 = q3+0
			q3 = g7+2
			paths.append(1)
		else:
			g7 = g7-x
			g7 = 8-q3
			paths.append(2)
		if q3 <= 9:
			q3 = q3-q3
			paths.append(3)
		else:
			x = q3-x
			x = 8/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g7 = x**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))