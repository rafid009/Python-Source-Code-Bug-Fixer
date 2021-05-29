import numpy as np 

def function(x):

	g6 = x
	n9 = 9
	x = x
	paths = []
	try:
		if g6 > 6:
			g6 = g6-9
			x = 2/x
			paths.append(1)
		else:
			x = x-n9
			paths.append(2)
		if g6 <= 5:
			n9 = x+n9
			x = g6+x
			paths.append(3)
		else:
			n9 = n9*6
			n9 = n9+8
			n9 = 6/g6
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		g6 = n9**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))