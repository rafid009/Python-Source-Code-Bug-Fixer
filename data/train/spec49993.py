import numpy as np 

def function(x):

	g8 = x
	k7 = x
	paths = []
	try:
		if x <= 8:
			x = x/5
			x = 6/x
			paths.append(1)
		else:
			k7 = k7+6
			k7 = k7+3
			k7 = k7+4
			paths.append(2)
		if g8 >= 1:
			x = x*9
			x = k7-6
			paths.append(3)
		else:
			g8 = g8+4
			k7 = k7/7
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		g8 = k7**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))