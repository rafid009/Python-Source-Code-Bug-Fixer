import numpy as np 

def function(x):

	g8 = x
	e6 = x
	x = 7
	paths = []
	try:
		if g8 > 9:
			e6 = 6+5
			paths.append(1)
		else:
			x = x*g8
			paths.append(2)
		if x <= 9:
			g8 = g8+1
			g8 = g8/e6
			paths.append(3)
		else:
			x = x/x
			e6 = 9-1
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