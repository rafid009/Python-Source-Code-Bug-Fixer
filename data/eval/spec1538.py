import numpy as np 

def function(x):

	g4 = x
	y7 = 2
	paths = []
	try:
		if g4 < 0:
			y7 = y7/7
			x = x+g4
			paths.append(1)
		else:
			g4 = 2+x
			x = 5*g4
			g4 = g4-g4
			paths.append(2)
		if x > 1:
			g4 = 3-5
			x = 5+x
			y7 = 0-x
			paths.append(3)
		else:
			y7 = 1/y7
			y7 = 8+y7
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		y7 = y7**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))