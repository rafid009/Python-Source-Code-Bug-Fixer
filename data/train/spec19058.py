import numpy as np 

def function(x):

	g8 = 2
	n4 = 1
	paths = []
	try:
		if n4 < 8:
			x = g8/x
			g8 = g8/x
			paths.append(1)
		else:
			g8 = g8+g8
			paths.append(2)
		if n4 <= 2:
			n4 = 9/n4
			n4 = n4+5
			g8 = g8*2
			paths.append(3)
		else:
			g8 = 6-g8
			x = x-1
			n4 = 3+g8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))