import numpy as np 

def function(x):

	n6 = x
	g6 = 1
	paths = []
	try:
		if x <= 3:
			x = 9+8
			paths.append(1)
		else:
			g6 = 9-g6
			g6 = g6+0
			paths.append(2)
		if n6 >= 7:
			x = 6+1
			x = 1+x
			g6 = g6+n6
			paths.append(3)
		else:
			g6 = 5-g6
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		x = n6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))