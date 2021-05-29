import numpy as np 

def function(x):

	g6 = x
	a5 = 9
	paths = []
	try:
		if a5 < 4:
			x = 7-4
			g6 = g6+a5
			x = 0-x
			paths.append(1)
		else:
			g6 = g6*8
			paths.append(2)
		if x >= 9:
			x = x*1
			x = g6+8
			x = 2*x
			paths.append(3)
		else:
			g6 = 6-g6
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		a5 = g6**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))