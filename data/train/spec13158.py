import numpy as np 

def function(x):

	d0 = x
	o6 = 2
	paths = []
	try:
		if o6 >= 7:
			d0 = 0*7
			paths.append(1)
		else:
			o6 = 4+d0
			paths.append(2)
		if x <= 4:
			d0 = 1/d0
			paths.append(3)
		else:
			o6 = o6*d0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d0 = x**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))