import numpy as np 

def function(x):

	g0 = x
	d7 = x
	paths = []
	try:
		if g0 < 9:
			d7 = 9-g0
			g0 = g0/3
			x = x/4
			paths.append(1)
		else:
			x = g0*d7
			g0 = g0/1
			x = x*x
			paths.append(2)
		if x > 5:
			x = 8+x
			g0 = g0-4
			paths.append(3)
		else:
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d7 = x**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))