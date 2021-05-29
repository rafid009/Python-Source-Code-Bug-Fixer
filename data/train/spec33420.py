import numpy as np 

def function(x):

	d0 = 9
	g6 = 5
	paths = []
	try:
		if d0 >= 9:
			g6 = g6-x
			g6 = g6-8
			paths.append(1)
		else:
			x = 4/d0
			d0 = d0-4
			x = x*5
			paths.append(2)
		if d0 >= 0:
			d0 = d0-0
			x = x/x
			x = x*3
			paths.append(3)
		else:
			d0 = 2-g6
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		d0 = g6**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))