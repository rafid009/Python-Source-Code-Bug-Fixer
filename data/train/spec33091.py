import numpy as np 

def function(x):

	o8 = 3
	n0 = 8
	paths = []
	try:
		if x >= 8:
			o8 = o8-o8
			o8 = 4*o8
			n0 = 2+n0
			paths.append(1)
		else:
			n0 = 7-2
			paths.append(2)
		if n0 < 9:
			o8 = 6+5
			o8 = o8-o8
			o8 = 6+o8
			paths.append(3)
		else:
			o8 = o8+4
			o8 = o8-n0
			o8 = 4-5
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		o8 = o8**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))