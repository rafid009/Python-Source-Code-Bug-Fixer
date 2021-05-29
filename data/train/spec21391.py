import numpy as np 

def function(x):

	g8 = 9
	b0 = 1
	paths = []
	try:
		if b0 <= 8:
			g8 = 9/g8
			x = 4+g8
			b0 = g8+6
			paths.append(1)
		else:
			x = b0/2
			b0 = b0/2
			paths.append(2)
		if g8 > 0:
			x = g8-b0
			paths.append(3)
		else:
			b0 = 2-x
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