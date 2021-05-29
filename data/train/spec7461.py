import numpy as np 

def function(x):

	k3 = 5
	g1 = x
	paths = []
	try:
		if x < 1:
			x = x-8
			k3 = 8+6
			paths.append(1)
		else:
			x = 8/6
			x = x+3
			paths.append(2)
		if x >= 8:
			g1 = 1/g1
			x = 3/6
			paths.append(3)
		else:
			x = 9+x
			x = 6-x
			k3 = k3/8
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