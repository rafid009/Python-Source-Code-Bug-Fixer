import numpy as np 

def function(x):

	g4 = 9
	n4 = 7
	paths = []
	try:
		if g4 < 4:
			x = x*n4
			paths.append(1)
		else:
			g4 = 9-0
			paths.append(2)
		if g4 >= 8:
			g4 = 9-g4
			g4 = 2/x
			paths.append(3)
		else:
			x = x-9
			g4 = g4/g4
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		x = g4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))