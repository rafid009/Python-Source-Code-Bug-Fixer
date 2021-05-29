import numpy as np 

def function(x):

	g6 = x
	b0 = x
	x = 6
	paths = []
	try:
		if b0 >= 1:
			g6 = g6/x
			g6 = g6+x
			g6 = g6/g6
			paths.append(1)
		else:
			x = x*x
			g6 = 7+g6
			paths.append(2)
		if g6 <= 5:
			g6 = 2*g6
			paths.append(3)
		else:
			x = x*4
			x = 0-4
			x = x*0
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		g6 = b0**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))