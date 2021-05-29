import numpy as np 

def function(x):

	g7 = x
	x9 = 4
	paths = []
	try:
		if x9 < 9:
			x9 = x9+8
			x9 = x+x9
			x = 3/x
			paths.append(1)
		else:
			x = x-1
			paths.append(2)
		if g7 >= 6:
			x9 = g7+x9
			x9 = x9-2
			x = x9/3
			paths.append(3)
		else:
			x = x*x
			g7 = g7+0
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		x9 = g7**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))