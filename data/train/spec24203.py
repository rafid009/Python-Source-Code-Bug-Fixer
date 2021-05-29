import numpy as np 

def function(x):

	w8 = x
	x5 = 8
	paths = []
	try:
		if x > 2:
			x5 = x5/2
			x = x-5
			x = x*9
			paths.append(1)
		else:
			x5 = x+0
			x = 9*9
			x = w8*9
			paths.append(2)
		if x < 3:
			w8 = x-6
			paths.append(3)
		else:
			x = 8-3
			w8 = x-5
			w8 = w8/4
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		w8 = x5**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))