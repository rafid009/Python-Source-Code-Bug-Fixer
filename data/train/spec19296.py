import numpy as np 

def function(x):

	d1 = 1
	o1 = x
	paths = []
	try:
		if x > 5:
			d1 = 5/o1
			x = x+5
			paths.append(1)
		else:
			d1 = 9-d1
			paths.append(2)
		if o1 < 9:
			o1 = 2-o1
			x = 2-o1
			paths.append(3)
		else:
			d1 = d1-4
			o1 = 5-5
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