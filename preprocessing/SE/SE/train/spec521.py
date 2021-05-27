import numpy as np 

def function(x):

	d0 = 9
	r9 = 2
	paths = []
	try:
		if d0 >= 2:
			d0 = 6/1
			r9 = r9+7
			r9 = 3-1
			paths.append(1)
		else:
			x = x/d0
			d0 = 9-d0
			r9 = r9*1
			paths.append(2)
		if d0 < 6:
			x = x-8
			paths.append(3)
		else:
			x = 3/x
			x = 6/x
			r9 = 3/r9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r9 = x**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))