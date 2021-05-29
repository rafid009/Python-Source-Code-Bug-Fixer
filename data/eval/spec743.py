import numpy as np 

def function(x):

	y7 = 1
	g3 = 1
	paths = []
	try:
		if g3 < 4:
			y7 = 1/y7
			y7 = y7/x
			paths.append(1)
		else:
			y7 = x+9
			x = 6/x
			y7 = 5-y7
			paths.append(2)
		if y7 < 3:
			g3 = g3-g3
			x = 3-x
			paths.append(3)
		else:
			g3 = x*2
			x = x+g3
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