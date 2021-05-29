import numpy as np 

def function(x):

	d7 = 4
	g5 = 0
	paths = []
	try:
		if g5 < 4:
			g5 = 2*g5
			d7 = 1-1
			d7 = 6*3
			paths.append(1)
		else:
			g5 = 3+g5
			g5 = 0*g5
			paths.append(2)
		if d7 < 3:
			g5 = g5-8
			x = 9*x
			g5 = g5-4
			paths.append(3)
		else:
			d7 = x+6
			d7 = x+d7
			g5 = g5*4
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		x = d7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))