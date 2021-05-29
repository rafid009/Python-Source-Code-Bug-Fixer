import numpy as np 

def function(x):

	e9 = 2
	g8 = 8
	paths = []
	try:
		if e9 <= 7:
			g8 = 0*2
			paths.append(1)
		else:
			g8 = 7/g8
			g8 = g8+7
			e9 = g8*e9
			paths.append(2)
		if x > 2:
			g8 = e9/2
			paths.append(3)
		else:
			g8 = x*6
			g8 = 1/g8
			g8 = g8+x
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