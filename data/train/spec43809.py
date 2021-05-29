import numpy as np 

def function(x):

	r6 = x
	g0 = x
	paths = []
	try:
		if g0 < 2:
			x = 0+1
			paths.append(1)
		else:
			x = x+4
			g0 = 3-g0
			x = 4-9
			paths.append(2)
		if x >= 2:
			g0 = 3/g0
			g0 = g0+7
			paths.append(3)
		else:
			g0 = g0-3
			x = x*5
			r6 = 3-r6
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		x = g0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))