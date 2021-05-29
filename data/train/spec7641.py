import numpy as np 

def function(x):

	g7 = x
	o4 = 0
	paths = []
	try:
		if o4 > 3:
			o4 = 9-o4
			o4 = 7-2
			o4 = 4*x
			paths.append(1)
		else:
			x = 9/x
			g7 = g7-3
			paths.append(2)
		if x < 9:
			o4 = o4-x
			g7 = 1+g7
			g7 = g7+6
			paths.append(3)
		else:
			g7 = 4/g7
			o4 = 1*o4
			g7 = 0+g7
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		g7 = o4**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))