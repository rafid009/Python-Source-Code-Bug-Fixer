import numpy as np 

def function(x):

	g1 = 6
	k1 = x
	paths = []
	try:
		if k1 < 1:
			k1 = g1/k1
			k1 = 9+x
			paths.append(1)
		else:
			g1 = g1/8
			k1 = k1+5
			paths.append(2)
		if g1 > 6:
			x = x+1
			paths.append(3)
		else:
			g1 = g1*4
			x = x-4
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		g1 = k1**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))