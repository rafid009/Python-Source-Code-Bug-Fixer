import numpy as np 

def function(x):

	g0 = 4
	d7 = x
	x = 8
	paths = []
	try:
		if x >= 6:
			x = 3+d7
			d7 = d7/8
			paths.append(1)
		else:
			g0 = 8-g0
			d7 = x-0
			paths.append(2)
		if d7 > 3:
			g0 = g0*2
			x = 1/x
			paths.append(3)
		else:
			g0 = 5+x
			d7 = d7+x
			d7 = g0-4
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		x = d7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))