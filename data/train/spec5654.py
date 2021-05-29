import numpy as np 

def function(x):

	o0 = x
	w8 = 9
	paths = []
	try:
		if w8 >= 9:
			w8 = 5+w8
			x = x*4
			paths.append(1)
		else:
			x = x*1
			x = x/w8
			paths.append(2)
		if x >= 5:
			w8 = w8*w8
			x = x+o0
			paths.append(3)
		else:
			x = w8/8
			x = x-3
			o0 = o0/3
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