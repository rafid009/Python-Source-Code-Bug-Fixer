import numpy as np 

def function(x):

	l3 = x
	g4 = 0
	paths = []
	try:
		if g4 <= 8:
			x = x-0
			g4 = l3+9
			paths.append(1)
		else:
			l3 = l3/4
			x = 7-l3
			paths.append(2)
		if g4 < 2:
			l3 = g4+4
			paths.append(3)
		else:
			x = 1-x
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