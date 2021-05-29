import numpy as np 

def function(x):

	d2 = x
	g0 = 1
	x = x
	paths = []
	try:
		if g0 >= 0:
			g0 = g0/6
			paths.append(1)
		else:
			x = x-0
			x = x-4
			x = 8*g0
			paths.append(2)
		if d2 > 1:
			g0 = 8/6
			x = 4-x
			paths.append(3)
		else:
			g0 = g0*5
			g0 = d2/6
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d2 = d2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))