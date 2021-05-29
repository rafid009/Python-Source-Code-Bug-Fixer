import numpy as np 

def function(x):

	w8 = 9
	b0 = 9
	paths = []
	try:
		if b0 >= 0:
			b0 = b0+3
			w8 = 6/w8
			paths.append(1)
		else:
			w8 = b0/w8
			paths.append(2)
		if x > 8:
			w8 = x-w8
			paths.append(3)
		else:
			b0 = 1-b0
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