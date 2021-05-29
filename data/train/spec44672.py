import numpy as np 

def function(x):

	g8 = 1
	i2 = 6
	paths = []
	try:
		if x < 2:
			g8 = g8+5
			g8 = x+0
			i2 = i2/1
			paths.append(1)
		else:
			i2 = i2*8
			paths.append(2)
		if x > 9:
			g8 = g8/x
			i2 = g8-2
			paths.append(3)
		else:
			i2 = g8/x
			g8 = 6*7
			i2 = 5/1
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