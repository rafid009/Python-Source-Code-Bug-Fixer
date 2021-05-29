import numpy as np 

def function(x):

	g1 = x
	e0 = 9
	paths = []
	try:
		if x < 6:
			e0 = e0*e0
			x = x+g1
			x = x/9
			paths.append(1)
		else:
			g1 = 5+e0
			x = g1/x
			paths.append(2)
		if x < 8:
			g1 = g1-x
			paths.append(3)
		else:
			e0 = e0-2
			g1 = g1/1
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		g1 = g1**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))