import numpy as np 

def function(x):

	w4 = x
	y1 = x
	paths = []
	try:
		if y1 >= 0:
			x = 1+0
			w4 = w4*9
			y1 = y1+x
			paths.append(1)
		else:
			w4 = w4/x
			x = w4/x
			w4 = w4*x
			paths.append(2)
		if x <= 7:
			x = x-8
			x = 2+x
			paths.append(3)
		else:
			x = x*w4
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