import numpy as np 

def function(x):

	g4 = x
	e0 = 7
	paths = []
	try:
		if e0 >= 1:
			g4 = g4+3
			paths.append(1)
		else:
			g4 = g4-5
			g4 = 2-3
			g4 = 9/g4
			paths.append(2)
		if g4 > 8:
			g4 = 5-g4
			g4 = g4+x
			e0 = 4-2
			paths.append(3)
		else:
			x = x*6
			e0 = 1*x
			g4 = g4/x
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		g4 = e0**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))