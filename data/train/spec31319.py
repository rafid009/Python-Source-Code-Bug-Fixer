import numpy as np 

def function(x):

	o7 = x
	d1 = x
	paths = []
	try:
		if o7 < 7:
			d1 = o7-d1
			d1 = 0/o7
			paths.append(1)
		else:
			o7 = o7/7
			o7 = 6/x
			paths.append(2)
		if x <= 7:
			x = 9/2
			x = x-o7
			paths.append(3)
		else:
			d1 = o7-d1
			x = 2/5
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