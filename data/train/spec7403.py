import numpy as np 

def function(x):

	k3 = 1
	g6 = 8
	paths = []
	try:
		if k3 >= 6:
			g6 = g6*8
			g6 = g6-g6
			k3 = 6-5
			paths.append(1)
		else:
			k3 = k3+8
			g6 = g6+9
			g6 = 5/g6
			paths.append(2)
		if x >= 2:
			g6 = g6-9
			x = x*5
			x = 8-x
			paths.append(3)
		else:
			x = x-7
			x = x+x
			x = k3+x
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		x = g6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))