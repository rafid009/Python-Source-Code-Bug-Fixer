import numpy as np 

def function(x):

	d6 = x
	g0 = 2
	paths = []
	try:
		if g0 > 8:
			d6 = 8-2
			x = d6*x
			paths.append(1)
		else:
			x = g0*x
			x = x*6
			x = 0+x
			paths.append(2)
		if x >= 4:
			g0 = d6+x
			x = x*6
			paths.append(3)
		else:
			g0 = g0/4
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		g0 = d6**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))