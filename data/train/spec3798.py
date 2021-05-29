import numpy as np 

def function(x):

	g7 = 9
	o7 = 4
	paths = []
	try:
		if o7 < 7:
			g7 = 0-6
			paths.append(1)
		else:
			o7 = o7/2
			x = x+5
			paths.append(2)
		if g7 < 6:
			o7 = 0-3
			g7 = g7-1
			o7 = g7-o7
			paths.append(3)
		else:
			x = x-o7
			o7 = o7/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))