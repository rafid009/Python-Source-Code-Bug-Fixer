import numpy as np 

def function(x):

	a8 = 3
	g5 = x
	paths = []
	try:
		if g5 <= 2:
			a8 = a8-0
			x = 7/x
			x = x-4
			paths.append(1)
		else:
			a8 = a8/9
			paths.append(2)
		if g5 < 9:
			g5 = a8-g5
			paths.append(3)
		else:
			x = g5-x
			g5 = 7/g5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))