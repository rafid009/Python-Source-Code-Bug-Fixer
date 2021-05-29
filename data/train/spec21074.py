import numpy as np 

def function(x):

	y2 = x
	w4 = 0
	paths = []
	try:
		if w4 >= 3:
			y2 = y2-1
			w4 = w4*y2
			paths.append(1)
		else:
			y2 = x*y2
			w4 = w4-1
			x = x/9
			paths.append(2)
		if y2 < 0:
			w4 = 0+w4
			y2 = x-1
			paths.append(3)
		else:
			x = w4*x
			x = 6-x
			x = 9*x
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))