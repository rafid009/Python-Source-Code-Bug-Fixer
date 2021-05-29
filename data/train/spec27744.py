import numpy as np 

def function(x):

	g6 = x
	o2 = x
	paths = []
	try:
		if g6 <= 8:
			x = x/x
			g6 = x+g6
			g6 = g6*8
			paths.append(1)
		else:
			x = x/g6
			paths.append(2)
		if x <= 9:
			x = 2*g6
			x = x-x
			paths.append(3)
		else:
			x = 3-x
			x = x+o2
			o2 = 5-o2
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		g6 = o2**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))