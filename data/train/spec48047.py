import numpy as np 

def function(x):

	i0 = 3
	g8 = 5
	x = 6
	paths = []
	try:
		if x >= 8:
			g8 = 1*6
			g8 = 4/3
			paths.append(1)
		else:
			g8 = 7/g8
			paths.append(2)
		if g8 >= 5:
			i0 = i0*x
			g8 = g8-x
			paths.append(3)
		else:
			x = x-9
			g8 = g8+8
			g8 = i0/g8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g8 = x**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))