import numpy as np 

def function(x):

	o9 = x
	g8 = x
	paths = []
	try:
		if g8 < 9:
			x = x/7
			g8 = 2+x
			x = x/3
			paths.append(1)
		else:
			o9 = 8+o9
			paths.append(2)
		if x <= 5:
			o9 = o9+0
			o9 = 6/g8
			paths.append(3)
		else:
			o9 = o9/g8
			g8 = g8+4
			g8 = g8-o9
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