import numpy as np 

def function(x):

	y2 = x
	h8 = x
	paths = []
	try:
		if y2 >= 5:
			y2 = 4/y2
			y2 = y2+2
			paths.append(1)
		else:
			x = 1*x
			y2 = y2*y2
			paths.append(2)
		if h8 <= 6:
			x = x/8
			x = 4+x
			paths.append(3)
		else:
			y2 = 4*7
			h8 = 8-h8
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