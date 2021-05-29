import numpy as np 

def function(x):

	d0 = 4
	g8 = x
	paths = []
	try:
		if d0 < 7:
			g8 = x+g8
			g8 = g8/3
			paths.append(1)
		else:
			d0 = 7+d0
			paths.append(2)
		if x > 4:
			g8 = 4-9
			paths.append(3)
		else:
			x = d0*g8
			g8 = 3*g8
			d0 = d0-8
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		g8 = d0**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))