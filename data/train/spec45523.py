import numpy as np 

def function(x):

	o4 = x
	g9 = x
	paths = []
	try:
		if g9 > 7:
			x = g9/x
			o4 = 2-9
			paths.append(1)
		else:
			g9 = g9-g9
			paths.append(2)
		if g9 > 3:
			x = 2+x
			g9 = o4/7
			paths.append(3)
		else:
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g9 = x**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))