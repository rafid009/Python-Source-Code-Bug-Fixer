import numpy as np 

def function(x):

	p4 = x
	g4 = 7
	paths = []
	try:
		if g4 > 1:
			p4 = 4/p4
			p4 = g4*1
			paths.append(1)
		else:
			g4 = g4-3
			p4 = 7-x
			g4 = 6*g4
			paths.append(2)
		if x <= 1:
			x = x-8
			paths.append(3)
		else:
			p4 = 6+3
			x = x/p4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g4 = x**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))