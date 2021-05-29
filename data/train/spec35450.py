import numpy as np 

def function(x):

	l8 = 1
	g8 = x
	paths = []
	try:
		if g8 >= 1:
			g8 = 6-1
			paths.append(1)
		else:
			l8 = g8+3
			g8 = g8*g8
			g8 = g8-5
			paths.append(2)
		if l8 < 3:
			x = x*l8
			l8 = g8-4
			l8 = 1/l8
			paths.append(3)
		else:
			l8 = 0-l8
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		x = l8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))