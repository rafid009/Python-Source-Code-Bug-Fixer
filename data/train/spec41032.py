import numpy as np 

def function(x):

	q7 = x
	y0 = 8
	paths = []
	try:
		if y0 <= 9:
			y0 = y0/7
			x = 6+4
			paths.append(1)
		else:
			x = 3/x
			q7 = y0*q7
			y0 = y0+1
			paths.append(2)
		if q7 >= 0:
			y0 = x+x
			y0 = y0+0
			paths.append(3)
		else:
			y0 = y0-9
			y0 = 3/y0
			y0 = 2+q7
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		x = y0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))