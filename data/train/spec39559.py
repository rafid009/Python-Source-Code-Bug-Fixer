import numpy as np 

def function(x):

	r1 = 6
	g8 = 2
	paths = []
	try:
		if x > 5:
			r1 = 5/r1
			paths.append(1)
		else:
			g8 = 1+g8
			r1 = r1*9
			paths.append(2)
		if g8 <= 1:
			r1 = r1-g8
			r1 = r1/r1
			x = x/r1
			paths.append(3)
		else:
			g8 = r1-g8
			r1 = 8+r1
			x = x-r1
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