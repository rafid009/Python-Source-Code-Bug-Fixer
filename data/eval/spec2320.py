import numpy as np 

def function(x):

	g9 = x
	g0 = 7
	paths = []
	try:
		if x < 5:
			x = g0+x
			g0 = g0-8
			g0 = 2*g0
			paths.append(1)
		else:
			g0 = 6*2
			paths.append(2)
		if g9 < 6:
			g0 = g0/7
			x = 4-x
			paths.append(3)
		else:
			g0 = g9/g9
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