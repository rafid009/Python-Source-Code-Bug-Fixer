import numpy as np 

def function(x):

	f4 = 5
	w0 = x
	paths = []
	try:
		if x >= 9:
			x = 9*x
			f4 = 2+f4
			x = f4-w0
			paths.append(1)
		else:
			f4 = f4/f4
			x = f4-w0
			w0 = f4-9
			paths.append(2)
		if f4 <= 8:
			x = x+8
			f4 = f4+8
			x = x-f4
			paths.append(3)
		else:
			x = 9-x
			w0 = x+w0
			f4 = f4-2
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