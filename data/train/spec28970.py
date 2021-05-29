import numpy as np 

def function(x):

	u7 = x
	g7 = 9
	paths = []
	try:
		if u7 > 3:
			u7 = x*4
			u7 = x+5
			paths.append(1)
		else:
			g7 = 9/g7
			g7 = g7+u7
			x = g7*x
			paths.append(2)
		if x >= 6:
			g7 = g7-g7
			paths.append(3)
		else:
			x = x-x
			g7 = 5-g7
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