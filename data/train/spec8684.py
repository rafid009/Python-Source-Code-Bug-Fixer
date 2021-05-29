import numpy as np 

def function(x):

	x8 = x
	g0 = 7
	paths = []
	try:
		if g0 < 4:
			g0 = g0-7
			x = x8+x
			paths.append(1)
		else:
			x = x8-1
			paths.append(2)
		if x <= 7:
			x = x8/x8
			paths.append(3)
		else:
			x = 1/4
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		g0 = x8**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))