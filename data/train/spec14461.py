import numpy as np 

def function(x):

	g7 = x
	x9 = 3
	paths = []
	try:
		if g7 <= 2:
			x = x/2
			x = x-7
			paths.append(1)
		else:
			x9 = g7+0
			paths.append(2)
		if x9 >= 7:
			g7 = 1/g7
			paths.append(3)
		else:
			x = 8/x
			x = x/3
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