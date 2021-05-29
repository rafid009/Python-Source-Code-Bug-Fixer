import numpy as np 

def function(x):

	o8 = x
	g8 = x
	paths = []
	try:
		if g8 > 7:
			x = o8*x
			g8 = g8+o8
			paths.append(1)
		else:
			x = 4-9
			x = 5+g8
			g8 = 7/3
			paths.append(2)
		if g8 > 6:
			x = x/x
			paths.append(3)
		else:
			g8 = 3*o8
			g8 = g8+x
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