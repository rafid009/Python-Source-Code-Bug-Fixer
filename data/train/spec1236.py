import numpy as np 

def function(x):

	g6 = 8
	u2 = 4
	paths = []
	try:
		if g6 > 5:
			x = x+6
			g6 = 9+g6
			u2 = u2-g6
			paths.append(1)
		else:
			x = 4+6
			g6 = 5-g6
			g6 = 3-u2
			paths.append(2)
		if x <= 7:
			x = x/u2
			x = x-1
			paths.append(3)
		else:
			g6 = g6-g6
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		u2 = u2**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))