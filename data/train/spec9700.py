import numpy as np 

def function(x):

	g6 = x
	a3 = 0
	paths = []
	try:
		if a3 <= 3:
			a3 = 7-a3
			paths.append(1)
		else:
			a3 = a3*6
			a3 = 8/9
			paths.append(2)
		if x < 8:
			a3 = a3/3
			g6 = 5*8
			paths.append(3)
		else:
			x = x-a3
			g6 = g6+7
			g6 = g6-g6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a3 = x**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))