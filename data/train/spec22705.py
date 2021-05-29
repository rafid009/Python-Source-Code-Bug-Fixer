import numpy as np 

def function(x):

	g0 = 1
	r6 = 9
	paths = []
	try:
		if r6 < 6:
			x = r6*5
			paths.append(1)
		else:
			g0 = 1-g0
			paths.append(2)
		if r6 >= 9:
			x = x+2
			r6 = r6-0
			r6 = g0/5
			paths.append(3)
		else:
			r6 = 2+r6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g0 = x**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))