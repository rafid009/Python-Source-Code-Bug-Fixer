import numpy as np 

def function(x):

	o0 = 6
	w4 = 2
	paths = []
	try:
		if w4 < 1:
			w4 = 4/7
			x = 1*x
			x = x-7
			paths.append(1)
		else:
			w4 = x+w4
			o0 = o0*6
			o0 = 8+o0
			paths.append(2)
		if x >= 7:
			w4 = x/2
			x = 0+3
			w4 = w4/w4
			paths.append(3)
		else:
			o0 = 0*o0
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