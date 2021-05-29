import numpy as np 

def function(x):

	x2 = 7
	o8 = 9
	paths = []
	try:
		if x2 < 4:
			x = 5-2
			paths.append(1)
		else:
			o8 = 0+o8
			paths.append(2)
		if x2 > 4:
			x2 = 5-x2
			paths.append(3)
		else:
			x2 = x2*6
			x2 = x2/4
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