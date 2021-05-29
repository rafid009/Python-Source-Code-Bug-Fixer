import numpy as np 

def function(x):

	g0 = x
	v0 = x
	paths = []
	try:
		if x < 8:
			g0 = v0*7
			v0 = 2/g0
			paths.append(1)
		else:
			g0 = 5/g0
			paths.append(2)
		if v0 > 0:
			g0 = g0-0
			g0 = g0-6
			paths.append(3)
		else:
			g0 = g0-2
			x = 9*v0
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		x = v0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))