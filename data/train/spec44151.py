import numpy as np 

def function(x):

	o8 = 8
	q3 = 9
	paths = []
	try:
		if q3 > 2:
			q3 = x/q3
			o8 = o8+x
			x = x/1
			paths.append(1)
		else:
			q3 = x-o8
			paths.append(2)
		if q3 > 8:
			o8 = o8-9
			q3 = q3/2
			o8 = o8+x
			paths.append(3)
		else:
			o8 = 1/4
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