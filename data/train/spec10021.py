import numpy as np 

def function(x):

	o8 = x
	f2 = x
	paths = []
	try:
		if o8 >= 1:
			o8 = 9-o8
			paths.append(1)
		else:
			f2 = 6*f2
			paths.append(2)
		if x > 7:
			f2 = 8-6
			paths.append(3)
		else:
			f2 = f2-o8
			x = 0+f2
			x = f2-2
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