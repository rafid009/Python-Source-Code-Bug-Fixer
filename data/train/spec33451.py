import numpy as np 

def function(x):

	d9 = 5
	g0 = 6
	paths = []
	try:
		if x >= 5:
			d9 = d9*6
			paths.append(1)
		else:
			g0 = 6/g0
			d9 = d9/d9
			d9 = g0-8
			paths.append(2)
		if g0 >= 4:
			d9 = d9/3
			paths.append(3)
		else:
			g0 = 0-g0
			x = x-2
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		g0 = d9**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))