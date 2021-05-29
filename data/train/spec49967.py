import numpy as np 

def function(x):

	o2 = x
	l8 = 5
	x = x
	paths = []
	try:
		if x < 8:
			l8 = l8-9
			x = x-0
			paths.append(1)
		else:
			o2 = 2*o2
			l8 = o2*1
			o2 = 7/o2
			paths.append(2)
		if o2 < 6:
			l8 = l8+o2
			l8 = 9/l8
			paths.append(3)
		else:
			l8 = 6*3
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		o2 = o2**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))