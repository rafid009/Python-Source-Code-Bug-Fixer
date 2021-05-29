import numpy as np 

def function(x):

	g9 = x
	k4 = 7
	paths = []
	try:
		if g9 < 6:
			k4 = 1/3
			k4 = 8-k4
			paths.append(1)
		else:
			k4 = 0*1
			k4 = x+7
			g9 = g9*3
			paths.append(2)
		if k4 >= 0:
			k4 = g9*k4
			g9 = g9-9
			paths.append(3)
		else:
			x = g9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))