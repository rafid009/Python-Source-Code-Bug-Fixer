import numpy as np 

def function(x):

	n3 = 4
	g4 = 7
	paths = []
	try:
		if g4 <= 9:
			g4 = n3/x
			paths.append(1)
		else:
			g4 = g4*3
			paths.append(2)
		if x > 3:
			g4 = n3-2
			x = g4-n3
			x = x*n3
			paths.append(3)
		else:
			x = x-x
			g4 = 6-g4
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		g4 = g4**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))