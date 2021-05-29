import numpy as np 

def function(x):

	g0 = 3
	k3 = x
	paths = []
	try:
		if g0 > 6:
			g0 = 1*3
			g0 = 1+2
			paths.append(1)
		else:
			k3 = x-7
			x = 8+x
			g0 = x-1
			paths.append(2)
		if g0 >= 7:
			g0 = 3-g0
			g0 = g0-k3
			g0 = g0/4
			paths.append(3)
		else:
			k3 = k3/6
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		k3 = g0**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))