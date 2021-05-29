import numpy as np 

def function(x):

	y1 = x
	g8 = x
	paths = []
	try:
		if g8 <= 1:
			y1 = g8-y1
			g8 = g8/2
			paths.append(1)
		else:
			g8 = 8*g8
			paths.append(2)
		if y1 >= 8:
			g8 = g8-8
			g8 = 4*2
			x = 2-7
			paths.append(3)
		else:
			g8 = g8/9
			x = 1/x
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