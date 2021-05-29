import numpy as np 

def function(x):

	e4 = x
	g7 = x
	paths = []
	try:
		if g7 > 8:
			x = 7*9
			g7 = 1*7
			paths.append(1)
		else:
			g7 = g7*4
			g7 = 3+g7
			paths.append(2)
		if g7 <= 4:
			x = g7+x
			x = x/1
			paths.append(3)
		else:
			x = 0/4
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