import numpy as np 

def function(x):

	g0 = x
	q6 = x
	paths = []
	try:
		if x > 6:
			x = 4-q6
			g0 = 0+g0
			g0 = x-1
			paths.append(1)
		else:
			g0 = 7+g0
			q6 = q6+5
			paths.append(2)
		if q6 > 6:
			g0 = x-x
			g0 = q6*g0
			paths.append(3)
		else:
			q6 = q6-2
			x = x-0
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