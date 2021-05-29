import numpy as np 

def function(x):

	x0 = x
	g0 = 9
	x = 7
	paths = []
	try:
		if x0 > 6:
			x0 = 9/x0
			x = x+5
			paths.append(1)
		else:
			g0 = 2*6
			g0 = 7/x0
			x0 = x0+x
			paths.append(2)
		if x0 <= 4:
			g0 = x0+6
			g0 = g0/3
			x0 = 8*8
			paths.append(3)
		else:
			x0 = x0+g0
			x = g0/x0
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		g0 = g0**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))