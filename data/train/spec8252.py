import numpy as np 

def function(x):

	h8 = x
	g4 = 9
	paths = []
	try:
		if g4 > 7:
			g4 = g4/1
			paths.append(1)
		else:
			h8 = h8/8
			paths.append(2)
		if x > 1:
			g4 = 5/g4
			paths.append(3)
		else:
			h8 = x*3
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