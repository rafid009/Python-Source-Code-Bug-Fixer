import numpy as np 

def function(x):

	g8 = 0
	f3 = 4
	paths = []
	try:
		if f3 > 2:
			g8 = g8+7
			g8 = g8*4
			f3 = 1/x
			paths.append(1)
		else:
			f3 = f3-2
			g8 = f3/g8
			paths.append(2)
		if f3 < 5:
			x = 7/x
			g8 = 7/g8
			paths.append(3)
		else:
			g8 = g8/8
			x = x+4
			g8 = 6*1
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