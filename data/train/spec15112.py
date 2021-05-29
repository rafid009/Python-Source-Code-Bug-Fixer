import numpy as np 

def function(x):

	w1 = x
	o7 = 3
	paths = []
	try:
		if o7 < 0:
			x = 1-x
			paths.append(1)
		else:
			o7 = o7-1
			paths.append(2)
		if o7 >= 9:
			o7 = 8*o7
			paths.append(3)
		else:
			o7 = x*o7
			o7 = 5-9
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))