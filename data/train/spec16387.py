import numpy as np 

def function(x):

	k1 = x
	g7 = 7
	paths = []
	try:
		if x < 0:
			g7 = 2*k1
			k1 = x-g7
			k1 = 6+k1
			paths.append(1)
		else:
			g7 = 4-g7
			x = x+4
			paths.append(2)
		if g7 >= 6:
			k1 = 3*3
			paths.append(3)
		else:
			k1 = k1+9
			x = k1-x
			g7 = 2/g7
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