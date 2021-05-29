import numpy as np 

def function(x):

	g5 = x
	y4 = 0
	x = x
	paths = []
	try:
		if g5 <= 7:
			y4 = y4-y4
			x = g5*5
			g5 = 8*y4
			paths.append(1)
		else:
			g5 = g5+y4
			g5 = g5/g5
			paths.append(2)
		if y4 < 3:
			y4 = y4-x
			x = g5*3
			paths.append(3)
		else:
			g5 = 1+6
			g5 = g5/g5
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		y4 = y4**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))