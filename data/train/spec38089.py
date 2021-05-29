import numpy as np 

def function(x):

	g5 = x
	d0 = 4
	paths = []
	try:
		if d0 >= 1:
			g5 = x/d0
			g5 = d0-g5
			paths.append(1)
		else:
			d0 = d0/5
			g5 = x/4
			paths.append(2)
		if g5 >= 6:
			x = 2/x
			x = x/x
			d0 = x-8
			paths.append(3)
		else:
			g5 = g5-d0
			d0 = 6-0
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		g5 = d0**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))