import numpy as np 

def function(x):

	b6 = 0
	g8 = 0
	paths = []
	try:
		if x > 7:
			g8 = g8+g8
			b6 = g8+5
			paths.append(1)
		else:
			b6 = 1*9
			paths.append(2)
		if b6 > 8:
			b6 = b6-x
			g8 = g8-3
			b6 = x*g8
			paths.append(3)
		else:
			x = 8+x
			x = x*7
			x = 5*x
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