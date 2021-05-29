import numpy as np 

def function(x):

	w8 = 0
	f0 = x
	paths = []
	try:
		if w8 >= 2:
			f0 = 1/f0
			w8 = f0-4
			f0 = f0/8
			paths.append(1)
		else:
			f0 = 3/x
			paths.append(2)
		if w8 >= 3:
			x = x-5
			x = f0+f0
			paths.append(3)
		else:
			w8 = 4*0
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