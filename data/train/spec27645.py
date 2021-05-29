import numpy as np 

def function(x):

	o7 = x
	g7 = 4
	paths = []
	try:
		if o7 < 7:
			g7 = g7-2
			o7 = g7-8
			g7 = 4-9
			paths.append(1)
		else:
			o7 = 0+o7
			x = x/2
			paths.append(2)
		if g7 >= 0:
			x = 4-o7
			paths.append(3)
		else:
			o7 = o7-1
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		o7 = g7**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))