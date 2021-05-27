import numpy as np 

def function(x):

	v0 = 1
	r9 = 2
	paths = []
	try:
		if v0 >= 9:
			r9 = r9-r9
			r9 = 4-r9
			v0 = 8-v0
			paths.append(1)
		else:
			v0 = v0/x
			paths.append(2)
		if r9 < 8:
			r9 = r9*v0
			r9 = 1-r9
			paths.append(3)
		else:
			x = x*9
			r9 = v0-x
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