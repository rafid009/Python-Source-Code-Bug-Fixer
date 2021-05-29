import numpy as np 

def function(x):

	o0 = x
	w4 = x
	paths = []
	try:
		if o0 > 5:
			o0 = w4-x
			o0 = o0+o0
			w4 = w4/2
			paths.append(1)
		else:
			x = x-6
			o0 = 0-o0
			o0 = 7-5
			paths.append(2)
		if w4 >= 8:
			o0 = o0+w4
			paths.append(3)
		else:
			o0 = x+o0
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))