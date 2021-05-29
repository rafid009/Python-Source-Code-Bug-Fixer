import numpy as np 

def function(x):

	x8 = 5
	g8 = x
	paths = []
	try:
		if x8 >= 8:
			x = g8/g8
			paths.append(1)
		else:
			x8 = x8/g8
			g8 = 9/9
			g8 = g8/2
			paths.append(2)
		if x < 3:
			g8 = 3*x
			g8 = g8/6
			x = x+9
			paths.append(3)
		else:
			x = x+2
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