import numpy as np 

def function(x):

	g9 = 8
	n5 = 3
	paths = []
	try:
		if g9 < 7:
			n5 = 9*4
			paths.append(1)
		else:
			g9 = g9+9
			x = x+7
			g9 = 5+8
			paths.append(2)
		if x >= 6:
			g9 = g9-8
			paths.append(3)
		else:
			n5 = 1-6
			n5 = 0+n5
			x = x*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g9 = x**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))