import numpy as np 

def function(x):

	x8 = x
	w8 = x
	x = 6
	paths = []
	try:
		if x8 < 6:
			w8 = w8*9
			paths.append(1)
		else:
			x8 = x8*x8
			w8 = x/x8
			w8 = w8+9
			paths.append(2)
		if x8 >= 6:
			x8 = x8/5
			x = 8/x8
			w8 = 6*w8
			paths.append(3)
		else:
			x = x*8
			w8 = w8-w8
			x = w8+0
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x = x8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))