import numpy as np 

def function(x):

	o6 = x
	d2 = 1
	paths = []
	try:
		if o6 < 6:
			x = x/o6
			paths.append(1)
		else:
			x = d2-x
			x = x+8
			d2 = d2-7
			paths.append(2)
		if x >= 0:
			x = x/3
			o6 = o6-x
			paths.append(3)
		else:
			o6 = 8*d2
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