import numpy as np 

def function(x):

	g0 = 6
	y2 = x
	paths = []
	try:
		if y2 < 5:
			x = x-x
			x = y2+7
			paths.append(1)
		else:
			y2 = y2*4
			paths.append(2)
		if g0 < 3:
			y2 = y2+g0
			paths.append(3)
		else:
			y2 = y2*x
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g0 = x**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))