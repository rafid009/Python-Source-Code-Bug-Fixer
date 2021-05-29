import numpy as np 

def function(x):

	o1 = x
	e7 = x
	paths = []
	try:
		if x >= 7:
			e7 = 8/8
			x = 5-0
			e7 = e7+o1
			paths.append(1)
		else:
			o1 = 1*9
			x = o1-x
			x = 6-5
			paths.append(2)
		if o1 <= 8:
			o1 = 7/x
			paths.append(3)
		else:
			x = x-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))