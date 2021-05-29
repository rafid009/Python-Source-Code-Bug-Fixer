import numpy as np 

def function(x):

	w8 = 1
	r9 = 3
	paths = []
	try:
		if w8 <= 2:
			r9 = r9/r9
			x = 8/x
			paths.append(1)
		else:
			x = 5*r9
			x = x+3
			paths.append(2)
		if w8 >= 7:
			r9 = r9/1
			w8 = r9/w8
			paths.append(3)
		else:
			w8 = w8-x
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		r9 = w8**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))