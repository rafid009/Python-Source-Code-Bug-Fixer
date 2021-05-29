import numpy as np 

def function(x):

	w5 = 5
	y2 = x
	x = 7
	paths = []
	try:
		if y2 > 1:
			x = y2-8
			paths.append(1)
		else:
			w5 = 7/x
			x = 5/x
			paths.append(2)
		if y2 > 1:
			w5 = w5+x
			paths.append(3)
		else:
			x = w5*x
			x = 5/x
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