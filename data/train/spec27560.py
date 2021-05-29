import numpy as np 

def function(x):

	r9 = x
	w0 = 9
	paths = []
	try:
		if x <= 9:
			r9 = 7+r9
			paths.append(1)
		else:
			r9 = r9+4
			x = 0-x
			x = x+2
			paths.append(2)
		if r9 < 0:
			w0 = r9-7
			r9 = r9/3
			paths.append(3)
		else:
			r9 = w0+8
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		r9 = r9**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))