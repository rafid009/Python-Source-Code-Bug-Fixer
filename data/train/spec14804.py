import numpy as np 

def function(x):

	g1 = x
	e8 = x
	paths = []
	try:
		if g1 >= 9:
			g1 = 1-g1
			g1 = 9+g1
			paths.append(1)
		else:
			g1 = x/6
			g1 = x/g1
			g1 = g1*5
			paths.append(2)
		if e8 >= 6:
			e8 = 4-e8
			paths.append(3)
		else:
			g1 = g1/2
			g1 = g1/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e8 = x**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))