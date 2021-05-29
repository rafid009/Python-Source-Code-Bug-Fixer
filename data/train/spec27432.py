import numpy as np 

def function(x):

	g8 = 5
	p9 = 4
	paths = []
	try:
		if p9 >= 0:
			x = p9/x
			g8 = 9/g8
			g8 = 7-4
			paths.append(1)
		else:
			p9 = 7-2
			paths.append(2)
		if x <= 3:
			g8 = g8*4
			x = 7/x
			g8 = g8*g8
			paths.append(3)
		else:
			g8 = 7-g8
			g8 = g8/g8
			x = x-x
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