import numpy as np 

def function(x):

	n7 = x
	g7 = 4
	paths = []
	try:
		if x < 4:
			x = x+4
			n7 = x-1
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if g7 >= 0:
			g7 = x/n7
			x = 8/x
			paths.append(3)
		else:
			x = 5-x
			n7 = x*n7
			x = x+0
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		g7 = g7**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))