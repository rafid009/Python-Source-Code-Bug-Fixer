import numpy as np 

def function(x):

	v6 = x
	g7 = 1
	paths = []
	try:
		if x <= 5:
			x = x+8
			paths.append(1)
		else:
			x = x-v6
			g7 = g7-x
			g7 = 0-v6
			paths.append(2)
		if x >= 8:
			x = g7*9
			paths.append(3)
		else:
			x = 7*g7
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