import numpy as np 

def function(x):

	g7 = x
	k0 = 2
	paths = []
	try:
		if g7 >= 0:
			g7 = g7*6
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if k0 > 2:
			g7 = k0/1
			k0 = 2*k0
			paths.append(3)
		else:
			k0 = k0/7
			k0 = 1+k0
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		x = g7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))