import numpy as np 

def function(x):

	n7 = 3
	g4 = 0
	paths = []
	try:
		if x <= 6:
			x = 9/x
			g4 = g4-g4
			g4 = g4*4
			paths.append(1)
		else:
			x = x-g4
			paths.append(2)
		if g4 <= 6:
			x = x+6
			n7 = n7/n7
			n7 = n7+4
			paths.append(3)
		else:
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g4 = x**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))