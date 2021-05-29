import numpy as np 

def function(x):

	g7 = x
	a4 = x
	paths = []
	try:
		if a4 <= 7:
			g7 = x*g7
			a4 = g7/9
			a4 = a4-3
			paths.append(1)
		else:
			a4 = a4*9
			paths.append(2)
		if a4 <= 1:
			x = 8*5
			paths.append(3)
		else:
			g7 = 8*x
			a4 = a4*a4
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