import numpy as np 

def function(x):

	v9 = 9
	g7 = 8
	paths = []
	try:
		if v9 > 1:
			x = x-2
			paths.append(1)
		else:
			x = 8-g7
			paths.append(2)
		if v9 >= 2:
			x = x/8
			g7 = 0/g7
			x = 4-x
			paths.append(3)
		else:
			x = 6-6
			v9 = v9+v9
			g7 = g7*3
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