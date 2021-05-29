import numpy as np 

def function(x):

	h6 = x
	y0 = x
	paths = []
	try:
		if x > 9:
			h6 = x*8
			h6 = y0/h6
			y0 = y0-y0
			paths.append(1)
		else:
			x = x-5
			paths.append(2)
		if y0 > 9:
			x = 0+h6
			y0 = 1-y0
			x = x*x
			paths.append(3)
		else:
			y0 = y0*2
			y0 = 3+y0
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