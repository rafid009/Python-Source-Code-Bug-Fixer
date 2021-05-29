import numpy as np 

def function(x):

	k7 = x
	g0 = 1
	paths = []
	try:
		if k7 >= 4:
			k7 = x-3
			k7 = 7-k7
			paths.append(1)
		else:
			x = 9*4
			x = 2/g0
			paths.append(2)
		if k7 <= 6:
			k7 = 6+k7
			g0 = g0-9
			paths.append(3)
		else:
			k7 = 9*k7
			k7 = 7*k7
			g0 = k7+6
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		g0 = k7**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))