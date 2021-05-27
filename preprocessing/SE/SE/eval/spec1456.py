import numpy as np 

def function(x):

	g8 = 3
	k2 = x
	x = 7
	paths = []
	try:
		if g8 >= 7:
			x = x/g8
			paths.append(1)
		else:
			k2 = g8-x
			paths.append(2)
		if g8 > 7:
			g8 = g8/g8
			paths.append(3)
		else:
			g8 = g8*1
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		x = k2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))