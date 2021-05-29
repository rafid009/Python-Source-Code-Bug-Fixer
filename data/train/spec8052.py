import numpy as np 

def function(x):

	k0 = x
	g6 = 6
	x = x
	paths = []
	try:
		if g6 >= 6:
			k0 = k0-1
			x = 3*x
			paths.append(1)
		else:
			g6 = 0-g6
			k0 = x/9
			x = x/6
			paths.append(2)
		if x >= 7:
			k0 = x+g6
			g6 = 9*g6
			paths.append(3)
		else:
			g6 = k0-7
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		g6 = k0**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))