import numpy as np 

def function(x):

	g0 = x
	y5 = 6
	paths = []
	try:
		if x > 4:
			g0 = g0/8
			y5 = y5*5
			y5 = y5*y5
			paths.append(1)
		else:
			g0 = 9+g0
			y5 = y5-2
			paths.append(2)
		if y5 <= 1:
			y5 = 7/y5
			y5 = y5/3
			g0 = g0/g0
			paths.append(3)
		else:
			y5 = g0/y5
			y5 = 6/5
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