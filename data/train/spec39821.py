import numpy as np 

def function(x):

	w4 = 0
	y2 = 8
	x = 2
	paths = []
	try:
		if x > 3:
			x = y2-8
			x = 3+0
			y2 = 4/y2
			paths.append(1)
		else:
			w4 = 1+w4
			y2 = 0/4
			x = w4-x
			paths.append(2)
		if y2 <= 1:
			w4 = 8+2
			paths.append(3)
		else:
			w4 = 5-w4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y2 = x**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))