import numpy as np 

def function(x):

	g7 = x
	r4 = x
	paths = []
	try:
		if r4 <= 7:
			x = r4+r4
			r4 = 5+8
			paths.append(1)
		else:
			r4 = 5-r4
			g7 = 3/g7
			paths.append(2)
		if r4 >= 5:
			g7 = g7-8
			paths.append(3)
		else:
			x = r4*6
			r4 = 0+r4
			r4 = 6/r4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))