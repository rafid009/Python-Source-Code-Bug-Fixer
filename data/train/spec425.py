import numpy as np 

def function(x):

	w3 = 0
	y6 = x
	paths = []
	try:
		if y6 <= 2:
			y6 = y6/y6
			w3 = 4*w3
			y6 = 3*y6
			paths.append(1)
		else:
			y6 = 7/5
			w3 = w3*8
			y6 = x-1
			paths.append(2)
		if x < 0:
			w3 = 8+w3
			w3 = 3-y6
			y6 = y6+5
			paths.append(3)
		else:
			x = 2/x
			w3 = 1/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y6 = x**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))