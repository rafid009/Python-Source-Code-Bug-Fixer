import numpy as np 

def function(x):

	g1 = x
	k3 = x
	paths = []
	try:
		if g1 >= 8:
			x = x-8
			x = 4-k3
			x = 7*x
			paths.append(1)
		else:
			x = 3*g1
			paths.append(2)
		if g1 < 4:
			g1 = g1+9
			g1 = g1/5
			paths.append(3)
		else:
			k3 = 7*9
			k3 = 2/k3
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		g1 = g1**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))