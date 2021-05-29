import numpy as np 

def function(x):

	b2 = x
	g9 = 0
	paths = []
	try:
		if g9 < 7:
			g9 = g9/3
			g9 = 1-g9
			paths.append(1)
		else:
			x = x+1
			g9 = g9*5
			b2 = 1+b2
			paths.append(2)
		if g9 >= 9:
			g9 = g9+4
			g9 = 8+4
			g9 = 6/1
			paths.append(3)
		else:
			x = x-7
			b2 = b2*x
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		g9 = b2**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))