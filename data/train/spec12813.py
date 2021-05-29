import numpy as np 

def function(x):

	y0 = 7
	d7 = x
	paths = []
	try:
		if d7 < 4:
			x = x*5
			paths.append(1)
		else:
			d7 = 2*d7
			y0 = 4/x
			paths.append(2)
		if x < 7:
			y0 = d7-x
			x = 7*2
			paths.append(3)
		else:
			d7 = d7-3
			y0 = y0-y0
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		y0 = y0**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))