import numpy as np 

def function(x):

	w8 = 1
	o0 = x
	paths = []
	try:
		if w8 <= 2:
			x = o0+w8
			o0 = o0*2
			w8 = w8+5
			paths.append(1)
		else:
			w8 = o0-w8
			paths.append(2)
		if o0 < 9:
			x = x*w8
			x = 8+x
			o0 = x/8
			paths.append(3)
		else:
			o0 = o0/2
			x = 0*8
			o0 = 7/o0
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