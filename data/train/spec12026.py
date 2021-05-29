import numpy as np 

def function(x):

	w8 = x
	f3 = 6
	paths = []
	try:
		if w8 <= 0:
			f3 = f3+w8
			f3 = x-2
			paths.append(1)
		else:
			x = f3*x
			w8 = 3-w8
			paths.append(2)
		if w8 >= 4:
			w8 = w8+w8
			x = 7*w8
			w8 = f3-3
			paths.append(3)
		else:
			w8 = w8*w8
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