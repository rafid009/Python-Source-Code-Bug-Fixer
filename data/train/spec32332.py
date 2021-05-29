import numpy as np 

def function(x):

	g3 = 8
	p2 = 2
	x = x
	paths = []
	try:
		if x > 7:
			p2 = x/4
			p2 = p2*x
			x = x+x
			paths.append(1)
		else:
			g3 = 8-p2
			x = g3*x
			paths.append(2)
		if x > 4:
			p2 = x+p2
			g3 = 9+x
			x = 3/4
			paths.append(3)
		else:
			p2 = 8/2
			g3 = 2*7
			g3 = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g3 = x**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))