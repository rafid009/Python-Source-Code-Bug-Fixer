import numpy as np 

def function(x):

	b0 = x
	g9 = 6
	paths = []
	try:
		if b0 >= 1:
			x = 4+x
			g9 = b0-g9
			x = x+1
			paths.append(1)
		else:
			x = 9*x
			x = x+x
			paths.append(2)
		if g9 >= 7:
			g9 = 2+g9
			x = x*x
			paths.append(3)
		else:
			g9 = g9-8
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		g9 = b0**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))