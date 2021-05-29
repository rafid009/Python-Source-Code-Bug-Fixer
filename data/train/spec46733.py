import numpy as np 

def function(x):

	o0 = x
	w8 = x
	paths = []
	try:
		if w8 > 7:
			x = x/3
			paths.append(1)
		else:
			o0 = o0*o0
			paths.append(2)
		if x > 6:
			x = x-w8
			w8 = 9/6
			paths.append(3)
		else:
			o0 = o0*o0
			x = 2*9
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