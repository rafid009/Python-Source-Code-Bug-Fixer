import numpy as np 

def function(x):

	k7 = x
	g8 = 2
	paths = []
	try:
		if k7 <= 0:
			x = 0-x
			x = x-x
			paths.append(1)
		else:
			k7 = 1+k7
			g8 = 5-0
			g8 = g8+g8
			paths.append(2)
		if g8 < 4:
			x = k7+4
			paths.append(3)
		else:
			x = 8*x
			g8 = g8*8
			g8 = k7-g8
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		x = k7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))