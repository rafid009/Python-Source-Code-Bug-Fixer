import numpy as np 

def function(x):

	x1 = x
	g7 = 5
	paths = []
	try:
		if x1 >= 1:
			g7 = 7*g7
			paths.append(1)
		else:
			g7 = g7*4
			g7 = g7-2
			x = x/2
			paths.append(2)
		if g7 < 1:
			x1 = 2+2
			x = 8-x
			x1 = 5+3
			paths.append(3)
		else:
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x1 = x1**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))