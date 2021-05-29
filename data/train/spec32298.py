import numpy as np 

def function(x):

	o8 = 3
	f3 = x
	paths = []
	try:
		if o8 <= 9:
			f3 = 3+9
			x = x/1
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if o8 >= 8:
			x = x/o8
			o8 = x/o8
			paths.append(3)
		else:
			f3 = 2-2
			o8 = 3+6
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