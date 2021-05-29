import numpy as np 

def function(x):

	n4 = x
	g9 = 4
	x = 2
	paths = []
	try:
		if n4 > 6:
			x = x/x
			paths.append(1)
		else:
			x = 7/n4
			g9 = 6-g9
			paths.append(2)
		if n4 >= 4:
			x = 0+6
			paths.append(3)
		else:
			g9 = g9/5
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		g9 = n4**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))