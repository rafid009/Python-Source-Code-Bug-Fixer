import numpy as np 

def function(x):

	j1 = 3
	g8 = x
	paths = []
	try:
		if j1 > 0:
			x = x-0
			j1 = 0/j1
			paths.append(1)
		else:
			x = 7-x
			paths.append(2)
		if g8 <= 9:
			j1 = j1-0
			g8 = 7-x
			g8 = 1*g8
			paths.append(3)
		else:
			j1 = 8*j1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g8 = x**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))