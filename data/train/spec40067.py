import numpy as np 

def function(x):

	w8 = x
	i0 = 2
	paths = []
	try:
		if w8 < 0:
			i0 = x/i0
			paths.append(1)
		else:
			w8 = x-9
			i0 = i0-i0
			w8 = w8+w8
			paths.append(2)
		if x > 8:
			w8 = 2/1
			paths.append(3)
		else:
			x = x-i0
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		x = i0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))