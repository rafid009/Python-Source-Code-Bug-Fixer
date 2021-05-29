import numpy as np 

def function(x):

	r5 = x
	y0 = 4
	paths = []
	try:
		if y0 <= 6:
			x = 7+x
			paths.append(1)
		else:
			x = x-0
			paths.append(2)
		if r5 >= 9:
			y0 = 5/y0
			paths.append(3)
		else:
			y0 = 8-y0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))