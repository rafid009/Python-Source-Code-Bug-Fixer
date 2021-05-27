import numpy as np 

def function(x):

	o8 = x
	w7 = 5
	paths = []
	try:
		if w7 <= 4:
			o8 = x*o8
			paths.append(1)
		else:
			x = w7/o8
			o8 = 4+o8
			paths.append(2)
		if o8 >= 4:
			x = 1-x
			w7 = x*w7
			o8 = 6+o8
			paths.append(3)
		else:
			o8 = 6+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o8 = x**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))