import numpy as np 

def function(x):

	w8 = 2
	r1 = 9
	paths = []
	try:
		if x < 9:
			x = x+1
			paths.append(1)
		else:
			w8 = 3*w8
			x = 8-4
			paths.append(2)
		if x < 6:
			w8 = x-6
			w8 = 3*w8
			x = 3*x
			paths.append(3)
		else:
			w8 = w8*4
			w8 = 9+w8
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