import numpy as np 

def function(x):

	g8 = 2
	d1 = 2
	paths = []
	try:
		if g8 > 2:
			g8 = 1-x
			g8 = 9*d1
			paths.append(1)
		else:
			x = g8-x
			g8 = g8-9
			paths.append(2)
		if g8 > 4:
			x = x+d1
			g8 = 7-g8
			g8 = g8*9
			paths.append(3)
		else:
			g8 = 4*g8
			x = 2-x
			x = d1*1
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