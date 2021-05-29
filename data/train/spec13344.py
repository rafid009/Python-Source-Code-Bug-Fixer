import numpy as np 

def function(x):

	g7 = 2
	i9 = 6
	paths = []
	try:
		if x > 5:
			g7 = 2-g7
			paths.append(1)
		else:
			g7 = 9+g7
			paths.append(2)
		if x < 0:
			x = i9*x
			paths.append(3)
		else:
			i9 = g7-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i9 = x**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))