import numpy as np 

def function(x):

	r2 = 1
	f1 = 1
	paths = []
	try:
		if f1 > 8:
			r2 = 3/r2
			paths.append(1)
		else:
			r2 = 3/x
			f1 = 0-f1
			paths.append(2)
		if x < 2:
			f1 = f1-5
			r2 = r2/r2
			r2 = f1-r2
			paths.append(3)
		else:
			r2 = r2+r2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r2 = x**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))