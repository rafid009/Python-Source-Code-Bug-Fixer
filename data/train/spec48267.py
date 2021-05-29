import numpy as np 

def function(x):

	g5 = 6
	d4 = x
	paths = []
	try:
		if x > 9:
			x = x*x
			d4 = 5+1
			g5 = g5+8
			paths.append(1)
		else:
			g5 = g5/7
			paths.append(2)
		if g5 < 0:
			x = x+g5
			paths.append(3)
		else:
			x = 2-x
			x = 7*7
			g5 = 9-g5
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		x = d4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))