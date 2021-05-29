import numpy as np 

def function(x):

	g8 = 1
	i0 = 0
	paths = []
	try:
		if x <= 4:
			i0 = 5*i0
			i0 = 0-7
			paths.append(1)
		else:
			x = x+x
			g8 = 3-g8
			paths.append(2)
		if g8 > 5:
			g8 = g8*x
			paths.append(3)
		else:
			g8 = g8/g8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))