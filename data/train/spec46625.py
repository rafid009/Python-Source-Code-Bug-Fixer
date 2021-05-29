import numpy as np 

def function(x):

	g4 = 9
	c2 = x
	paths = []
	try:
		if x >= 3:
			g4 = g4+g4
			paths.append(1)
		else:
			g4 = g4+7
			g4 = 4+x
			paths.append(2)
		if c2 > 4:
			x = x/1
			paths.append(3)
		else:
			g4 = g4*g4
			g4 = 8/g4
			g4 = x/6
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