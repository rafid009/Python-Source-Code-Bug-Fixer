import numpy as np 

def function(x):

	d3 = x
	g6 = x
	x = x
	paths = []
	try:
		if x >= 2:
			g6 = 9+x
			paths.append(1)
		else:
			x = 7+x
			g6 = 5/d3
			g6 = 5*g6
			paths.append(2)
		if x > 5:
			g6 = 3-g6
			x = x*6
			x = 9+x
			paths.append(3)
		else:
			g6 = g6+5
			g6 = g6/6
			g6 = g6*0
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		x = g6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))