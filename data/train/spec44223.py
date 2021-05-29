import numpy as np 

def function(x):

	a2 = 8
	g7 = x
	paths = []
	try:
		if g7 >= 9:
			a2 = a2-9
			a2 = a2/5
			g7 = x-3
			paths.append(1)
		else:
			a2 = 4-a2
			paths.append(2)
		if g7 <= 1:
			a2 = a2-9
			paths.append(3)
		else:
			a2 = 5-a2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g7 = x**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))