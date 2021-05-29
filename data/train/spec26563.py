import numpy as np 

def function(x):

	p4 = x
	g5 = x
	x = x
	paths = []
	try:
		if x >= 0:
			g5 = g5+4
			paths.append(1)
		else:
			x = x-0
			p4 = p4/g5
			paths.append(2)
		if p4 < 4:
			g5 = 6*4
			paths.append(3)
		else:
			p4 = 9/p4
			x = 1/g5
			p4 = p4*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))