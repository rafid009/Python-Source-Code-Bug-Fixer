import numpy as np 

def function(x):

	t4 = x
	o8 = x
	paths = []
	try:
		if t4 < 0:
			o8 = 6+5
			paths.append(1)
		else:
			o8 = o8/t4
			x = 8*o8
			x = x+t4
			paths.append(2)
		if o8 > 7:
			o8 = x+t4
			x = o8+6
			paths.append(3)
		else:
			x = x-9
			o8 = o8+t4
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