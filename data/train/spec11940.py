import numpy as np 

def function(x):

	x0 = 4
	o1 = x
	paths = []
	try:
		if x0 >= 9:
			o1 = o1-o1
			o1 = 2+o1
			x0 = 7+x0
			paths.append(1)
		else:
			x0 = x0*o1
			paths.append(2)
		if x < 5:
			x = 1-3
			x = x-5
			o1 = x0*o1
			paths.append(3)
		else:
			x = 0*x0
			o1 = 8/o1
			x = x+4
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		o1 = x0**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))