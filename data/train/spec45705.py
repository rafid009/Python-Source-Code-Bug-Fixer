import numpy as np 

def function(x):

	g9 = 8
	b5 = 7
	paths = []
	try:
		if x < 9:
			g9 = 6/6
			x = 0-x
			paths.append(1)
		else:
			g9 = g9*3
			x = 7+x
			g9 = g9+9
			paths.append(2)
		if g9 <= 3:
			x = x+7
			paths.append(3)
		else:
			x = 8*x
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