import numpy as np 

def function(x):

	g0 = x
	k1 = x
	paths = []
	try:
		if g0 > 2:
			g0 = g0-9
			x = k1-x
			paths.append(1)
		else:
			k1 = 0-k1
			k1 = 0*k1
			paths.append(2)
		if g0 >= 6:
			k1 = k1*3
			paths.append(3)
		else:
			g0 = k1*g0
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))