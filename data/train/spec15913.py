import numpy as np 

def function(x):

	r8 = 2
	g8 = 9
	paths = []
	try:
		if g8 <= 1:
			r8 = r8*5
			g8 = g8+4
			x = x+x
			paths.append(1)
		else:
			r8 = 4+r8
			g8 = g8-0
			paths.append(2)
		if x > 8:
			r8 = 4*g8
			x = x/2
			g8 = g8+r8
			paths.append(3)
		else:
			g8 = 3-r8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g8 = x**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))