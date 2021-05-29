import numpy as np 

def function(x):

	f0 = 7
	y0 = 2
	paths = []
	try:
		if y0 < 8:
			y0 = 1-y0
			paths.append(1)
		else:
			x = x*8
			y0 = y0+f0
			y0 = 1-2
			paths.append(2)
		if y0 < 9:
			x = f0/x
			paths.append(3)
		else:
			f0 = x+x
			y0 = f0-3
			y0 = y0-0
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