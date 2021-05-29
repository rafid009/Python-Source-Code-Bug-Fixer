import numpy as np 

def function(x):

	g7 = x
	i7 = x
	paths = []
	try:
		if x < 2:
			x = i7-x
			g7 = g7+9
			i7 = i7-1
			paths.append(1)
		else:
			g7 = 4*8
			x = x/6
			paths.append(2)
		if g7 < 9:
			x = i7+9
			g7 = 7+3
			paths.append(3)
		else:
			i7 = x-g7
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