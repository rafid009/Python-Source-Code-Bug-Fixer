import numpy as np 

def function(x):

	o8 = 2
	v4 = x
	paths = []
	try:
		if o8 <= 8:
			v4 = 2/v4
			o8 = o8/x
			paths.append(1)
		else:
			o8 = v4+8
			x = 1*o8
			v4 = x-4
			paths.append(2)
		if v4 >= 5:
			x = 6*x
			v4 = o8+3
			x = 5+v4
			paths.append(3)
		else:
			v4 = 2/v4
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