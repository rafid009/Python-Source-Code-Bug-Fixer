import numpy as np 

def function(x):

	d0 = x
	g1 = 8
	paths = []
	try:
		if g1 > 8:
			g1 = g1+x
			x = x+5
			d0 = d0+8
			paths.append(1)
		else:
			g1 = 3/g1
			paths.append(2)
		if d0 < 0:
			g1 = 8*g1
			paths.append(3)
		else:
			x = x/4
			g1 = 8/g1
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		g1 = d0**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))