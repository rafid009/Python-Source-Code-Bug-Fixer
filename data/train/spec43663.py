import numpy as np 

def function(x):

	g7 = 7
	a6 = 5
	paths = []
	try:
		if x <= 2:
			g7 = g7+3
			a6 = 7+1
			x = x+1
			paths.append(1)
		else:
			a6 = g7+1
			x = 4-0
			paths.append(2)
		if g7 > 7:
			g7 = 4-7
			x = x-4
			paths.append(3)
		else:
			x = 2*7
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