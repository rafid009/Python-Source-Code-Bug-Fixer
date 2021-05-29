import numpy as np 

def function(x):

	g9 = 8
	y3 = x
	paths = []
	try:
		if y3 <= 0:
			y3 = y3/x
			x = x-1
			paths.append(1)
		else:
			x = x-8
			g9 = x+6
			g9 = g9*y3
			paths.append(2)
		if g9 >= 6:
			x = 6+g9
			x = 2-x
			g9 = g9/g9
			paths.append(3)
		else:
			y3 = 8*y3
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