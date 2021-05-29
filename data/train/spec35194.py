import numpy as np 

def function(x):

	r9 = 2
	o0 = 8
	paths = []
	try:
		if x > 9:
			r9 = 3+r9
			x = 0*r9
			paths.append(1)
		else:
			x = x-3
			r9 = r9/8
			paths.append(2)
		if o0 > 3:
			o0 = 5/o0
			r9 = 3/r9
			paths.append(3)
		else:
			r9 = 9+1
			r9 = 3*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o0 = x**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))