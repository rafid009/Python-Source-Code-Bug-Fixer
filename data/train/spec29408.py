import numpy as np 

def function(x):

	w8 = x
	d1 = 8
	paths = []
	try:
		if w8 < 1:
			x = x-9
			d1 = d1-0
			d1 = 8+w8
			paths.append(1)
		else:
			x = 8+x
			paths.append(2)
		if x > 0:
			x = x-7
			x = 7/x
			paths.append(3)
		else:
			w8 = x-d1
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		x = w8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))