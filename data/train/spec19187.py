import numpy as np 

def function(x):

	d2 = x
	o8 = 7
	paths = []
	try:
		if o8 < 3:
			o8 = x/x
			x = x/2
			x = x*4
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if x >= 2:
			d2 = o8/d2
			paths.append(3)
		else:
			x = 3+x
			d2 = 5-2
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