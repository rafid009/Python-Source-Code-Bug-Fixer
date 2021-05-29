import numpy as np 

def function(x):

	o1 = 7
	o8 = 7
	paths = []
	try:
		if o1 <= 6:
			o8 = o8-x
			o1 = o1*9
			paths.append(1)
		else:
			o8 = 0-o8
			paths.append(2)
		if x > 7:
			o1 = o1-o1
			x = 7-9
			paths.append(3)
		else:
			x = 0/1
			o1 = o8-o1
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