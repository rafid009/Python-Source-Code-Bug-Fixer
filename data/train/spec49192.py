import numpy as np 

def function(x):

	g8 = x
	y4 = 6
	paths = []
	try:
		if y4 < 9:
			x = x/x
			x = x/x
			y4 = y4*y4
			paths.append(1)
		else:
			g8 = 4-0
			paths.append(2)
		if g8 < 8:
			y4 = x-6
			y4 = y4+6
			paths.append(3)
		else:
			y4 = y4*9
			g8 = g8*x
			g8 = g8+8
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		x = g8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))