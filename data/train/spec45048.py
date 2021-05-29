import numpy as np 

def function(x):

	g4 = 1
	p9 = x
	paths = []
	try:
		if p9 < 1:
			g4 = 7/8
			p9 = 3-4
			p9 = 5+g4
			paths.append(1)
		else:
			g4 = g4+g4
			paths.append(2)
		if x < 8:
			x = 4-p9
			p9 = p9/x
			paths.append(3)
		else:
			g4 = g4-g4
			p9 = p9/7
			g4 = g4/6
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