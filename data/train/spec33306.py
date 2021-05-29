import numpy as np 

def function(x):

	r4 = 3
	g1 = x
	paths = []
	try:
		if x > 9:
			g1 = 7+x
			g1 = g1+0
			x = x+7
			paths.append(1)
		else:
			g1 = g1*r4
			paths.append(2)
		if g1 >= 7:
			g1 = g1/5
			r4 = x-3
			g1 = g1-1
			paths.append(3)
		else:
			x = x/r4
			r4 = r4-6
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		g1 = r4**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))