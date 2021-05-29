import numpy as np 

def function(x):

	w0 = x
	f9 = 2
	paths = []
	try:
		if w0 > 3:
			w0 = 2-7
			f9 = f9+6
			paths.append(1)
		else:
			f9 = 0/f9
			paths.append(2)
		if f9 >= 8:
			x = w0+7
			x = 6-0
			x = w0/7
			paths.append(3)
		else:
			w0 = w0/3
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