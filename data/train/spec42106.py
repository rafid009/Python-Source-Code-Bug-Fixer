import numpy as np 

def function(x):

	g7 = x
	r9 = 9
	paths = []
	try:
		if x < 7:
			g7 = g7/x
			paths.append(1)
		else:
			g7 = 3+g7
			x = 2+x
			r9 = r9-4
			paths.append(2)
		if x < 3:
			g7 = g7-8
			paths.append(3)
		else:
			r9 = r9/r9
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		x = g7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))