import numpy as np 

def function(x):

	j9 = x
	g0 = x
	paths = []
	try:
		if g0 <= 5:
			g0 = g0-1
			j9 = j9/j9
			paths.append(1)
		else:
			j9 = 9*g0
			paths.append(2)
		if g0 > 0:
			g0 = 4-g0
			g0 = 4-g0
			paths.append(3)
		else:
			x = 9+x
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