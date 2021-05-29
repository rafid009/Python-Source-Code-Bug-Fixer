import numpy as np 

def function(x):

	k3 = 0
	g6 = 4
	x = 9
	paths = []
	try:
		if x < 6:
			g6 = g6+k3
			x = 8-x
			paths.append(1)
		else:
			x = k3-x
			k3 = 7+k3
			paths.append(2)
		if g6 < 0:
			x = 8*x
			paths.append(3)
		else:
			g6 = g6+x
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		k3 = g6**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))