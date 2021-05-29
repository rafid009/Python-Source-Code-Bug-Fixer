import numpy as np 

def function(x):

	g0 = x
	a8 = x
	paths = []
	try:
		if g0 >= 3:
			a8 = a8+5
			paths.append(1)
		else:
			g0 = 8/8
			g0 = 2/x
			paths.append(2)
		if x > 4:
			x = a8*1
			paths.append(3)
		else:
			x = 3/3
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