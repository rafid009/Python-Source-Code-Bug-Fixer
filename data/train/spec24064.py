import numpy as np 

def function(x):

	h1 = 7
	y0 = x
	paths = []
	try:
		if y0 > 9:
			y0 = y0/h1
			paths.append(1)
		else:
			y0 = h1+9
			y0 = y0*8
			paths.append(2)
		if x >= 2:
			y0 = y0*1
			paths.append(3)
		else:
			h1 = h1-y0
			x = 2-4
			y0 = y0*y0
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		y0 = h1**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))