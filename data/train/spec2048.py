import numpy as np 

def function(x):

	b3 = x
	g3 = x
	paths = []
	try:
		if x < 5:
			x = x-2
			b3 = 5-5
			paths.append(1)
		else:
			b3 = 0-2
			b3 = b3/4
			paths.append(2)
		if x <= 6:
			x = x+x
			g3 = g3-2
			paths.append(3)
		else:
			g3 = g3-5
			g3 = g3-3
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