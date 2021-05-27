import numpy as np 

def function(x):

	o8 = x
	a6 = x
	x = x
	paths = []
	try:
		if x < 8:
			o8 = 7*o8
			x = x-0
			paths.append(1)
		else:
			a6 = x/a6
			paths.append(2)
		if a6 < 0:
			x = x*6
			a6 = a6*o8
			o8 = x-4
			paths.append(3)
		else:
			o8 = o8-a6
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