import numpy as np 

def function(x):

	b6 = 7
	g8 = 9
	paths = []
	try:
		if g8 > 8:
			g8 = g8/8
			paths.append(1)
		else:
			x = x*1
			x = x*9
			b6 = x-b6
			paths.append(2)
		if b6 <= 1:
			g8 = 7+g8
			g8 = b6/2
			b6 = g8-4
			paths.append(3)
		else:
			x = 2-3
			g8 = 9+g8
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