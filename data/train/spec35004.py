import numpy as np 

def function(x):

	w6 = x
	y0 = x
	x = x
	paths = []
	try:
		if x <= 0:
			x = w6-7
			paths.append(1)
		else:
			w6 = w6/8
			paths.append(2)
		if y0 > 1:
			y0 = y0+y0
			y0 = y0*x
			paths.append(3)
		else:
			y0 = y0*7
			y0 = y0*9
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		y0 = w6**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))