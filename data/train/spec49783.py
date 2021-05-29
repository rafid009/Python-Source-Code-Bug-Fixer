import numpy as np 

def function(x):

	g0 = x
	x8 = 3
	paths = []
	try:
		if g0 > 5:
			g0 = 4*1
			x8 = x8/5
			paths.append(1)
		else:
			g0 = 0-g0
			x8 = 4-0
			paths.append(2)
		if g0 <= 9:
			x8 = 3/x8
			x = x+7
			paths.append(3)
		else:
			x8 = g0-1
			x8 = 8-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))