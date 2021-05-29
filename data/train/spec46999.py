import numpy as np 

def function(x):

	g3 = 3
	p2 = x
	paths = []
	try:
		if p2 < 1:
			g3 = g3/x
			paths.append(1)
		else:
			x = x+3
			x = x+x
			paths.append(2)
		if p2 >= 1:
			g3 = x/5
			paths.append(3)
		else:
			p2 = p2*x
			g3 = g3/4
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