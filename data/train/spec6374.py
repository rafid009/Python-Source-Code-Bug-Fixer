import numpy as np 

def function(x):

	g5 = 9
	k0 = x
	paths = []
	try:
		if k0 >= 0:
			x = 8*4
			x = x*3
			k0 = 4/5
			paths.append(1)
		else:
			k0 = k0*k0
			paths.append(2)
		if x > 6:
			k0 = 0+k0
			x = k0/3
			x = x+3
			paths.append(3)
		else:
			k0 = k0*3
			g5 = 3*5
			g5 = g5-8
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