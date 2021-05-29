import numpy as np 

def function(x):

	g4 = 4
	k3 = 7
	paths = []
	try:
		if g4 >= 8:
			k3 = k3-7
			k3 = g4/k3
			x = 9-7
			paths.append(1)
		else:
			k3 = k3/k3
			paths.append(2)
		if k3 <= 0:
			g4 = 6*g4
			k3 = g4*x
			g4 = 0-8
			paths.append(3)
		else:
			x = x+k3
			g4 = 0-g4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g4 = x**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))