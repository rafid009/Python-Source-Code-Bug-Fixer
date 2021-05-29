import numpy as np 

def function(x):

	g8 = x
	h6 = x
	x = x
	paths = []
	try:
		if x >= 5:
			g8 = 6*g8
			g8 = h6-g8
			paths.append(1)
		else:
			g8 = g8-g8
			paths.append(2)
		if g8 >= 7:
			g8 = x/g8
			h6 = h6-g8
			g8 = 2*0
			paths.append(3)
		else:
			x = h6+h6
			x = h6-x
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