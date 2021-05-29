import numpy as np 

def function(x):

	k1 = x
	g1 = 6
	paths = []
	try:
		if x >= 6:
			k1 = k1*k1
			x = 1-5
			paths.append(1)
		else:
			k1 = 3-7
			x = x/2
			x = 6/x
			paths.append(2)
		if g1 < 4:
			g1 = 2+g1
			k1 = 5/7
			k1 = k1+7
			paths.append(3)
		else:
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g1 = x**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))