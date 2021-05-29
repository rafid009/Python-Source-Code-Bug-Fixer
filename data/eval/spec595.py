import numpy as np 

def function(x):

	x0 = 2
	w8 = 4
	x = x
	paths = []
	try:
		if x < 0:
			x0 = 3-3
			w8 = 1+3
			paths.append(1)
		else:
			w8 = w8*9
			x0 = x0/7
			paths.append(2)
		if w8 >= 2:
			x0 = x0+x0
			w8 = 6*w8
			paths.append(3)
		else:
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))