import numpy as np 

def function(x):

	f8 = x
	d1 = 7
	paths = []
	try:
		if x <= 6:
			x = 7/f8
			x = x-d1
			paths.append(1)
		else:
			x = x/8
			f8 = x-5
			f8 = f8*f8
			paths.append(2)
		if f8 <= 9:
			f8 = f8-5
			paths.append(3)
		else:
			f8 = f8+7
			f8 = 0/f8
			d1 = 9*f8
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