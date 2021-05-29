import numpy as np 

def function(x):

	g7 = 9
	x8 = x
	paths = []
	try:
		if x <= 5:
			g7 = x*g7
			paths.append(1)
		else:
			x = 1+8
			x = x*x
			paths.append(2)
		if x <= 8:
			x8 = 0/x8
			g7 = g7+5
			paths.append(3)
		else:
			g7 = g7-0
			x8 = g7-8
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		g7 = g7**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))