import numpy as np 

def function(x):

	b0 = x
	g0 = 2
	paths = []
	try:
		if g0 >= 6:
			b0 = 5-g0
			g0 = g0*b0
			g0 = x-x
			paths.append(1)
		else:
			g0 = g0/x
			paths.append(2)
		if b0 >= 8:
			x = x-1
			b0 = x-b0
			x = 0*x
			paths.append(3)
		else:
			x = g0+x
			b0 = b0+9
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		g0 = g0**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))