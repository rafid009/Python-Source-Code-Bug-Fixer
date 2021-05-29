import numpy as np 

def function(x):

	n9 = 0
	g6 = 5
	paths = []
	try:
		if g6 > 6:
			x = x*6
			paths.append(1)
		else:
			g6 = 9/x
			g6 = 4*g6
			n9 = n9*8
			paths.append(2)
		if g6 > 7:
			n9 = n9*g6
			x = 0/3
			x = 3-x
			paths.append(3)
		else:
			x = 9-x
			x = x/4
			g6 = 0-g6
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		n9 = g6**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))