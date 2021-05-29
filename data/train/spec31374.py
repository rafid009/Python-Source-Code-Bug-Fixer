import numpy as np 

def function(x):

	g7 = x
	r7 = 6
	paths = []
	try:
		if x <= 4:
			x = x+7
			paths.append(1)
		else:
			g7 = g7+6
			paths.append(2)
		if x <= 4:
			r7 = 9+8
			x = 2/x
			paths.append(3)
		else:
			x = x+5
			g7 = g7*x
			r7 = r7/x
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