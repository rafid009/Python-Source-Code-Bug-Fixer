import numpy as np 

def function(x):

	o5 = 0
	o8 = x
	x = x
	paths = []
	try:
		if o5 < 1:
			o5 = 1*o5
			o8 = 6*o8
			paths.append(1)
		else:
			o5 = o5+2
			o8 = 9+7
			paths.append(2)
		if x <= 5:
			o5 = 5+o5
			paths.append(3)
		else:
			o8 = o5+8
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