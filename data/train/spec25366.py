import numpy as np 

def function(x):

	g6 = x
	e0 = 5
	paths = []
	try:
		if g6 < 9:
			x = x+8
			x = 0-x
			e0 = 4+6
			paths.append(1)
		else:
			g6 = g6*x
			x = x*g6
			paths.append(2)
		if e0 < 2:
			e0 = e0*4
			g6 = g6/g6
			paths.append(3)
		else:
			g6 = g6*1
			e0 = 4-e0
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		e0 = g6**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))