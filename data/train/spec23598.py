import numpy as np 

def function(x):

	d2 = 9
	g0 = x
	paths = []
	try:
		if d2 >= 2:
			x = x-d2
			paths.append(1)
		else:
			g0 = g0*x
			d2 = d2-g0
			paths.append(2)
		if d2 < 7:
			x = 7+x
			d2 = d2/2
			paths.append(3)
		else:
			g0 = 0-d2
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		d2 = g0**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))