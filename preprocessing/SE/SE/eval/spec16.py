import numpy as np 

def function(x):

	o2 = x
	o6 = 2
	paths = []
	try:
		if o2 >= 0:
			o6 = 0*8
			o2 = o2-o6
			x = 8/x
			paths.append(1)
		else:
			o2 = 8*o2
			o2 = 0+o2
			o6 = o6*3
			paths.append(2)
		if o2 >= 0:
			o2 = o2-o2
			paths.append(3)
		else:
			o6 = o6*o6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o2 = x**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))