import numpy as np 

def function(x):

	g1 = x
	h8 = x
	paths = []
	try:
		if x <= 5:
			x = x/8
			g1 = 0+h8
			paths.append(1)
		else:
			x = x/x
			g1 = 5+g1
			g1 = g1+h8
			paths.append(2)
		if g1 < 1:
			g1 = g1*5
			h8 = h8-h8
			paths.append(3)
		else:
			h8 = h8/h8
			x = 4-0
			h8 = h8*2
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