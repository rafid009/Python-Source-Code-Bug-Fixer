import numpy as np 

def function(x):

	g7 = 2
	u0 = x
	paths = []
	try:
		if g7 < 0:
			g7 = g7-5
			x = x/3
			x = x+0
			paths.append(1)
		else:
			g7 = g7/4
			u0 = u0/u0
			g7 = 5+5
			paths.append(2)
		if g7 > 3:
			u0 = 2-7
			g7 = 1-7
			paths.append(3)
		else:
			x = x*g7
			x = x+2
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