import numpy as np 

def function(x):

	g1 = 1
	k7 = x
	paths = []
	try:
		if k7 >= 3:
			g1 = g1-9
			x = x*9
			k7 = 1/x
			paths.append(1)
		else:
			x = x-g1
			paths.append(2)
		if g1 <= 2:
			g1 = g1-5
			g1 = 9+g1
			k7 = 7*g1
			paths.append(3)
		else:
			x = 4-k7
			x = 3/7
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		x = g1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))