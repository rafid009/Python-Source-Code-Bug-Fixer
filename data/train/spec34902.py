import numpy as np 

def function(x):

	n7 = x
	g1 = 2
	paths = []
	try:
		if g1 > 6:
			x = 8/3
			g1 = 6*7
			paths.append(1)
		else:
			x = 6*x
			paths.append(2)
		if g1 > 3:
			n7 = n7*4
			paths.append(3)
		else:
			x = x+n7
			g1 = g1/n7
			n7 = 2/n7
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		g1 = g1**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))