import numpy as np 

def function(x):

	y1 = x
	g8 = x
	paths = []
	try:
		if y1 < 7:
			y1 = y1+3
			y1 = 8-y1
			x = 8/y1
			paths.append(1)
		else:
			g8 = 9*g8
			x = x-0
			g8 = g8+0
			paths.append(2)
		if y1 >= 7:
			x = 3-x
			y1 = 8-2
			x = g8+0
			paths.append(3)
		else:
			x = y1*g8
			y1 = 7/2
			y1 = y1/9
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		g8 = g8**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))