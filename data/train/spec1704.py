import numpy as np 

def function(x):

	e4 = 6
	g1 = 1
	paths = []
	try:
		if x >= 4:
			g1 = 6-9
			paths.append(1)
		else:
			e4 = e4+5
			g1 = 8/e4
			x = 8/x
			paths.append(2)
		if x <= 8:
			e4 = 6*x
			x = x/6
			e4 = e4*2
			paths.append(3)
		else:
			g1 = g1+g1
			e4 = 4+e4
			g1 = 5-7
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