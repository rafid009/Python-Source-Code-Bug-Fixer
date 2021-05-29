import numpy as np 

def function(x):

	g8 = 7
	d2 = 2
	paths = []
	try:
		if d2 <= 1:
			x = 1/3
			x = g8+2
			g8 = g8*2
			paths.append(1)
		else:
			x = g8-x
			paths.append(2)
		if x > 8:
			g8 = x-g8
			x = g8*g8
			paths.append(3)
		else:
			d2 = 3/7
			x = x/5
			g8 = g8-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d2 = x**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))