import numpy as np 

def function(x):

	o0 = x
	w9 = x
	paths = []
	try:
		if w9 <= 3:
			x = 7-0
			x = x*w9
			x = o0-x
			paths.append(1)
		else:
			x = o0*9
			o0 = 2/3
			paths.append(2)
		if o0 < 4:
			o0 = o0*3
			x = 3-x
			paths.append(3)
		else:
			w9 = w9+7
			x = 6-w9
			w9 = o0*x
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