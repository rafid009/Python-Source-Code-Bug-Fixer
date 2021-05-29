import numpy as np 

def function(x):

	f4 = x
	g6 = 0
	paths = []
	try:
		if f4 < 7:
			g6 = 8+6
			paths.append(1)
		else:
			x = x-g6
			paths.append(2)
		if f4 < 0:
			g6 = g6*3
			x = x*4
			x = 7+f4
			paths.append(3)
		else:
			g6 = 3+x
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		g6 = f4**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))