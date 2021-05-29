import numpy as np 

def function(x):

	r2 = 2
	f1 = 8
	paths = []
	try:
		if x >= 2:
			f1 = x/r2
			r2 = r2*6
			paths.append(1)
		else:
			f1 = r2-r2
			r2 = 7-0
			paths.append(2)
		if r2 <= 5:
			x = x-0
			r2 = 1-4
			paths.append(3)
		else:
			x = 8*x
			f1 = x+r2
			r2 = r2/x
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