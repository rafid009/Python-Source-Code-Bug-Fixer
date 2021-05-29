import numpy as np 

def function(x):

	a8 = x
	g7 = x
	paths = []
	try:
		if g7 >= 0:
			g7 = a8/g7
			x = 5+5
			paths.append(1)
		else:
			x = 5+5
			paths.append(2)
		if x < 8:
			g7 = g7-2
			x = 3-x
			x = 5/a8
			paths.append(3)
		else:
			g7 = x-4
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		g7 = a8**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))