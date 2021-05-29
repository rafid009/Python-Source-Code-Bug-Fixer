import numpy as np 

def function(x):

	g6 = 6
	o5 = x
	paths = []
	try:
		if g6 >= 0:
			x = 9-x
			paths.append(1)
		else:
			g6 = g6-7
			x = x+x
			o5 = o5*x
			paths.append(2)
		if x <= 4:
			o5 = o5/g6
			o5 = 7/o5
			g6 = g6-5
			paths.append(3)
		else:
			x = 7+x
			g6 = x-7
			o5 = o5+5
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