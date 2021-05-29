import numpy as np 

def function(x):

	g0 = x
	k4 = x
	paths = []
	try:
		if k4 <= 3:
			x = x+7
			k4 = k4-4
			paths.append(1)
		else:
			g0 = g0-g0
			paths.append(2)
		if x <= 0:
			g0 = g0*g0
			x = 3+6
			paths.append(3)
		else:
			g0 = 3*4
			k4 = 7/k4
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		k4 = k4**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))