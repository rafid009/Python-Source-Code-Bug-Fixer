import numpy as np 

def function(x):

	g8 = 8
	i4 = x
	paths = []
	try:
		if g8 <= 4:
			x = 8*g8
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if g8 < 4:
			g8 = 0*4
			x = x*7
			paths.append(3)
		else:
			g8 = g8-5
			x = x/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))