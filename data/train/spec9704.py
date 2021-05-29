import numpy as np 

def function(x):

	g7 = x
	b5 = 8
	paths = []
	try:
		if b5 < 3:
			x = x*8
			x = x+g7
			x = 3-g7
			paths.append(1)
		else:
			g7 = g7-6
			paths.append(2)
		if g7 < 8:
			b5 = 1/g7
			paths.append(3)
		else:
			b5 = b5+5
			x = 3*6
			x = x*6
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