import numpy as np 

def function(x):

	g6 = 9
	e4 = x
	paths = []
	try:
		if g6 <= 9:
			e4 = x*2
			g6 = 9/5
			paths.append(1)
		else:
			g6 = g6/x
			x = x-3
			paths.append(2)
		if g6 >= 6:
			g6 = g6/1
			e4 = e4*e4
			paths.append(3)
		else:
			g6 = x/3
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		e4 = e4**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))