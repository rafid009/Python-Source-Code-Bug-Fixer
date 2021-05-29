import numpy as np 

def function(x):

	g8 = 7
	x2 = x
	paths = []
	try:
		if x2 >= 7:
			x = x+5
			g8 = 8+g8
			x = x-2
			paths.append(1)
		else:
			g8 = 8+g8
			paths.append(2)
		if g8 < 5:
			x2 = 0-x2
			x = 9+x
			g8 = g8+0
			paths.append(3)
		else:
			g8 = g8*7
			g8 = 4+3
			x = x2-x2
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x = x2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))