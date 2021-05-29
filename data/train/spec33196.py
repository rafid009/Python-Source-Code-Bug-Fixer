import numpy as np 

def function(x):

	v0 = x
	g0 = x
	paths = []
	try:
		if v0 < 9:
			g0 = 3+5
			v0 = 7+v0
			paths.append(1)
		else:
			v0 = 2*v0
			x = x-2
			v0 = x+8
			paths.append(2)
		if v0 >= 9:
			x = 0-x
			paths.append(3)
		else:
			x = 7*7
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		g0 = v0**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))