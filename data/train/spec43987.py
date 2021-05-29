import numpy as np 

def function(x):

	g6 = x
	d7 = x
	paths = []
	try:
		if g6 > 7:
			d7 = d7-9
			g6 = g6*4
			d7 = d7-3
			paths.append(1)
		else:
			d7 = d7+d7
			g6 = x/8
			paths.append(2)
		if g6 > 2:
			d7 = d7+2
			d7 = d7-g6
			paths.append(3)
		else:
			d7 = 4-4
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		d7 = d7**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))