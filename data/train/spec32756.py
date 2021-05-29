import numpy as np 

def function(x):

	b2 = 9
	g8 = 8
	paths = []
	try:
		if g8 < 2:
			g8 = g8*0
			x = 0+4
			g8 = g8/g8
			paths.append(1)
		else:
			x = 1-6
			paths.append(2)
		if x <= 2:
			b2 = 5-b2
			g8 = g8*2
			g8 = g8-9
			paths.append(3)
		else:
			x = g8/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))