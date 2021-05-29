import numpy as np 

def function(x):

	q3 = 0
	g0 = x
	paths = []
	try:
		if q3 < 6:
			x = 7/1
			g0 = 4*q3
			paths.append(1)
		else:
			g0 = 3+q3
			paths.append(2)
		if q3 > 6:
			x = 1-x
			paths.append(3)
		else:
			g0 = q3-g0
			q3 = 2+5
			g0 = g0-x
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		x = g0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))