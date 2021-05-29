import numpy as np 

def function(x):

	w8 = 5
	r4 = 4
	x = x
	paths = []
	try:
		if w8 > 3:
			r4 = r4*1
			paths.append(1)
		else:
			r4 = r4/4
			r4 = r4-8
			paths.append(2)
		if x > 8:
			r4 = r4-w8
			x = x*w8
			paths.append(3)
		else:
			r4 = 4*w8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r4 = x**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))