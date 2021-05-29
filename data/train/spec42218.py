import numpy as np 

def function(x):

	y8 = 0
	g5 = 3
	paths = []
	try:
		if y8 <= 9:
			x = 4/g5
			y8 = y8/x
			g5 = g5-g5
			paths.append(1)
		else:
			x = x-0
			paths.append(2)
		if y8 > 1:
			g5 = 2-y8
			paths.append(3)
		else:
			x = x-2
			y8 = y8-5
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		g5 = y8**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))