import numpy as np 

def function(x):

	k0 = x
	g5 = x
	paths = []
	try:
		if x < 1:
			g5 = 7/x
			x = x-8
			k0 = x+1
			paths.append(1)
		else:
			g5 = g5*5
			g5 = g5+1
			paths.append(2)
		if k0 >= 7:
			g5 = g5/9
			x = 9-5
			k0 = k0*4
			paths.append(3)
		else:
			g5 = 7/1
			g5 = x/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))