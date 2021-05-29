import numpy as np 

def function(x):

	x8 = 8
	g5 = 9
	paths = []
	try:
		if x8 < 9:
			x = g5+x
			paths.append(1)
		else:
			g5 = 7+g5
			paths.append(2)
		if x >= 8:
			g5 = x-g5
			x8 = 8+x8
			g5 = g5-3
			paths.append(3)
		else:
			x8 = x8/x
			x8 = x8-2
			g5 = g5-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x8 = x**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))