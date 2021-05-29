import numpy as np 

def function(x):

	d7 = x
	o1 = 2
	paths = []
	try:
		if d7 > 0:
			o1 = 9-d7
			d7 = o1-4
			paths.append(1)
		else:
			d7 = d7*o1
			x = x+2
			paths.append(2)
		if o1 > 6:
			o1 = x+7
			paths.append(3)
		else:
			d7 = d7/x
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