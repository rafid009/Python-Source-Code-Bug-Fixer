import numpy as np 

def function(x):

	g8 = x
	y6 = x
	paths = []
	try:
		if y6 > 5:
			x = 7*1
			y6 = g8/y6
			g8 = 7-g8
			paths.append(1)
		else:
			g8 = y6/y6
			paths.append(2)
		if y6 < 9:
			g8 = 4/y6
			g8 = 2-5
			y6 = y6*5
			paths.append(3)
		else:
			y6 = 5-y6
			x = 5*g8
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		y6 = y6**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))