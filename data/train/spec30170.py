import numpy as np 

def function(x):

	o8 = 5
	f8 = 3
	paths = []
	try:
		if x >= 7:
			o8 = 3/o8
			paths.append(1)
		else:
			o8 = o8-4
			paths.append(2)
		if o8 >= 4:
			f8 = f8+7
			paths.append(3)
		else:
			x = 9/x
			f8 = f8+9
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