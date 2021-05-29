import numpy as np 

def function(x):

	g5 = 4
	x1 = 0
	paths = []
	try:
		if g5 < 6:
			g5 = 5+7
			x1 = 1+0
			paths.append(1)
		else:
			x1 = x1/9
			x = 5-x
			paths.append(2)
		if g5 >= 3:
			g5 = x-2
			paths.append(3)
		else:
			x1 = x1/x1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))