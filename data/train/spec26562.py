import numpy as np 

def function(x):

	y0 = 6
	h6 = x
	paths = []
	try:
		if x > 2:
			x = h6/1
			y0 = y0*7
			paths.append(1)
		else:
			y0 = x*y0
			paths.append(2)
		if y0 > 3:
			y0 = 2+0
			h6 = h6*1
			h6 = h6/3
			paths.append(3)
		else:
			y0 = 9*y0
			h6 = 2*h6
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		y0 = h6**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))