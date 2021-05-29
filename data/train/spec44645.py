import numpy as np 

def function(x):

	g8 = 2
	v5 = 5
	paths = []
	try:
		if x > 4:
			g8 = 9-g8
			paths.append(1)
		else:
			x = x+6
			g8 = g8-x
			x = 4*g8
			paths.append(2)
		if v5 > 1:
			x = x+8
			g8 = x+g8
			paths.append(3)
		else:
			g8 = g8/x
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		x = g8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))