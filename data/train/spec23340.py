import numpy as np 

def function(x):

	r5 = 6
	x4 = x
	paths = []
	try:
		if r5 > 9:
			r5 = 6*x
			x = x-x4
			x4 = 6-x4
			paths.append(1)
		else:
			r5 = r5-5
			paths.append(2)
		if x > 0:
			x4 = x4+x4
			x = 3*7
			x4 = 5/x4
			paths.append(3)
		else:
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		r5 = x4**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))