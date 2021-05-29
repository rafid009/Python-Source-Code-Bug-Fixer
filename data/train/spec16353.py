import numpy as np 

def function(x):

	q8 = 4
	g7 = x
	paths = []
	try:
		if g7 <= 2:
			g7 = g7*9
			g7 = x+7
			q8 = 1-4
			paths.append(1)
		else:
			q8 = 3*5
			paths.append(2)
		if g7 >= 0:
			g7 = g7+8
			x = q8-x
			q8 = q8/g7
			paths.append(3)
		else:
			g7 = g7*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))