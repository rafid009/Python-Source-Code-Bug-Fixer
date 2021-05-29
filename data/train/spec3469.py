import numpy as np 

def function(x):

	v5 = 0
	o7 = 0
	paths = []
	try:
		if x <= 0:
			o7 = o7+v5
			paths.append(1)
		else:
			x = 3-o7
			x = 7*o7
			paths.append(2)
		if x > 5:
			o7 = o7+6
			paths.append(3)
		else:
			o7 = x/8
			o7 = o7-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))