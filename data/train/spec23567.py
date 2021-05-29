import numpy as np 

def function(x):

	g6 = 6
	y2 = 9
	paths = []
	try:
		if x > 0:
			y2 = 7-8
			x = x*6
			paths.append(1)
		else:
			g6 = y2+6
			x = y2+x
			paths.append(2)
		if g6 < 9:
			x = g6-1
			g6 = 4-g6
			paths.append(3)
		else:
			x = x+9
			g6 = x/1
			y2 = y2/7
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		y2 = y2**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))