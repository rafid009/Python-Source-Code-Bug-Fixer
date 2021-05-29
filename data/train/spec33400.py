import numpy as np 

def function(x):

	i0 = 4
	g7 = x
	x = 4
	paths = []
	try:
		if g7 >= 9:
			x = x+1
			x = 3/x
			x = 0+x
			paths.append(1)
		else:
			g7 = 3-9
			i0 = i0-i0
			g7 = 4/g7
			paths.append(2)
		if g7 < 7:
			i0 = g7-0
			x = 0-x
			paths.append(3)
		else:
			i0 = 6*9
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		g7 = i0**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))