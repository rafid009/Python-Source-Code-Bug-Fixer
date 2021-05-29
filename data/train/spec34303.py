import numpy as np 

def function(x):

	g1 = 8
	p4 = 5
	paths = []
	try:
		if x >= 8:
			x = 9*4
			paths.append(1)
		else:
			x = x/4
			g1 = g1*x
			paths.append(2)
		if g1 >= 9:
			p4 = p4-3
			paths.append(3)
		else:
			g1 = g1-2
			x = x+4
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