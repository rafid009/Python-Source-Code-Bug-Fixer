import numpy as np 

def function(x):

	g7 = x
	o9 = 8
	paths = []
	try:
		if g7 < 8:
			o9 = x/5
			x = x+o9
			paths.append(1)
		else:
			o9 = o9/8
			x = 8*o9
			x = 4-x
			paths.append(2)
		if x <= 9:
			x = x/7
			o9 = o9/o9
			paths.append(3)
		else:
			g7 = g7+2
			o9 = o9-o9
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