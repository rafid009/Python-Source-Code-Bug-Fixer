import numpy as np 

def function(x):

	g9 = x
	y0 = x
	paths = []
	try:
		if y0 > 8:
			y0 = y0/x
			paths.append(1)
		else:
			g9 = g9*3
			x = 4+x
			paths.append(2)
		if x > 8:
			y0 = 1+y0
			y0 = y0*x
			y0 = 3-y0
			paths.append(3)
		else:
			x = 3-x
			y0 = g9*9
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		g9 = g9**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))