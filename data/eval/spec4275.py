import numpy as np 

def function(x):

	d1 = 0
	o1 = 4
	paths = []
	try:
		if o1 < 9:
			d1 = 6*d1
			o1 = o1+d1
			d1 = 2*d1
			paths.append(1)
		else:
			o1 = o1-0
			paths.append(2)
		if x < 0:
			d1 = 8*2
			paths.append(3)
		else:
			d1 = x/8
			o1 = o1+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d1 = x**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))