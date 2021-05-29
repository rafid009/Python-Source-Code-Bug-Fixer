import numpy as np 

def function(x):

	y7 = 8
	w7 = x
	paths = []
	try:
		if w7 <= 8:
			y7 = 6*w7
			paths.append(1)
		else:
			w7 = w7+w7
			x = 9*x
			w7 = w7/3
			paths.append(2)
		if x > 2:
			w7 = 9-0
			y7 = 1+y7
			paths.append(3)
		else:
			x = x/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))