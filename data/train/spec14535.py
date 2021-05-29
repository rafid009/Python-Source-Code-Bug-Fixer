import numpy as np 

def function(x):

	e8 = 0
	g6 = x
	paths = []
	try:
		if x >= 6:
			e8 = e8-1
			paths.append(1)
		else:
			g6 = x/4
			x = x-4
			paths.append(2)
		if e8 >= 3:
			g6 = g6/g6
			paths.append(3)
		else:
			g6 = g6*8
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		e8 = g6**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))