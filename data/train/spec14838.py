import numpy as np 

def function(x):

	g8 = 0
	e9 = 2
	paths = []
	try:
		if g8 <= 9:
			g8 = g8/8
			g8 = g8+5
			paths.append(1)
		else:
			e9 = g8*7
			x = g8*g8
			paths.append(2)
		if g8 < 4:
			g8 = g8+x
			x = x/2
			g8 = g8*7
			paths.append(3)
		else:
			e9 = e9/6
			x = 6*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))