import numpy as np 

def function(x):

	v7 = x
	g0 = x
	paths = []
	try:
		if x <= 0:
			v7 = v7-x
			paths.append(1)
		else:
			g0 = 9/g0
			v7 = 2-v7
			x = x*7
			paths.append(2)
		if g0 <= 9:
			g0 = g0/4
			paths.append(3)
		else:
			g0 = x/6
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		g0 = g0**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))