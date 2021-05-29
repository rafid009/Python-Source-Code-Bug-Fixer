import numpy as np 

def function(x):

	g9 = x
	g5 = 8
	paths = []
	try:
		if x >= 7:
			g5 = g5*g9
			g9 = g9-2
			g9 = 7-g5
			paths.append(1)
		else:
			g5 = g5/9
			g5 = g5*5
			paths.append(2)
		if g9 <= 3:
			g9 = 6+4
			paths.append(3)
		else:
			g5 = g5*g9
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