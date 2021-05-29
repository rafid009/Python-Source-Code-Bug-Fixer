import numpy as np 

def function(x):

	g3 = 1
	r4 = 2
	paths = []
	try:
		if g3 < 8:
			r4 = 1-r4
			g3 = g3*4
			paths.append(1)
		else:
			r4 = r4-g3
			paths.append(2)
		if x > 5:
			g3 = g3/7
			x = 1+r4
			g3 = x-r4
			paths.append(3)
		else:
			r4 = 2-r4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r4 = x**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))