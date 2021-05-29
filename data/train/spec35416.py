import numpy as np 

def function(x):

	g8 = x
	i8 = 6
	paths = []
	try:
		if i8 <= 1:
			g8 = 7-g8
			paths.append(1)
		else:
			x = x/2
			x = 5/x
			i8 = i8-x
			paths.append(2)
		if i8 >= 3:
			i8 = i8-i8
			paths.append(3)
		else:
			g8 = 5-x
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