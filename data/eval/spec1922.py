import numpy as np 

def function(x):

	u0 = 8
	g4 = 4
	paths = []
	try:
		if u0 <= 3:
			g4 = g4/g4
			paths.append(1)
		else:
			u0 = x/3
			paths.append(2)
		if g4 > 4:
			g4 = x/g4
			u0 = u0-u0
			paths.append(3)
		else:
			g4 = 4*g4
			x = x+6
			x = x/8
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