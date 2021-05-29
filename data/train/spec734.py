import numpy as np 

def function(x):

	e8 = 9
	g7 = x
	paths = []
	try:
		if g7 < 1:
			e8 = 7/e8
			g7 = 2-g7
			paths.append(1)
		else:
			x = x-g7
			e8 = 9/e8
			paths.append(2)
		if x > 8:
			x = 9+1
			g7 = 1-3
			e8 = e8*9
			paths.append(3)
		else:
			e8 = 6/e8
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