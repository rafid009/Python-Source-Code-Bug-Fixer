import numpy as np 

def function(x):

	g5 = 0
	l8 = x
	x = x
	paths = []
	try:
		if l8 <= 9:
			l8 = x/2
			x = x-8
			paths.append(1)
		else:
			g5 = g5/1
			g5 = g5-9
			paths.append(2)
		if g5 > 9:
			l8 = l8*g5
			l8 = l8*6
			paths.append(3)
		else:
			l8 = l8-2
			l8 = 5*g5
			g5 = l8+g5
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