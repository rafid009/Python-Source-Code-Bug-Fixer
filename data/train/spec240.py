import numpy as np 

def function(x):

	a2 = 7
	g6 = x
	paths = []
	try:
		if a2 >= 3:
			g6 = a2*1
			x = 2*x
			paths.append(1)
		else:
			a2 = 7-5
			g6 = a2-1
			paths.append(2)
		if g6 < 3:
			g6 = 1+6
			x = 1-x
			paths.append(3)
		else:
			a2 = a2*5
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