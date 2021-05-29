import numpy as np 

def function(x):

	g6 = 4
	o4 = x
	paths = []
	try:
		if g6 > 7:
			x = x*g6
			paths.append(1)
		else:
			o4 = 1/o4
			paths.append(2)
		if g6 > 6:
			x = 8+x
			x = x/1
			o4 = o4/o4
			paths.append(3)
		else:
			g6 = 4/g6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g6 = x**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))