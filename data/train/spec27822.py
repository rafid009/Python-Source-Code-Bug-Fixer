import numpy as np 

def function(x):

	x7 = 5
	o7 = x
	paths = []
	try:
		if o7 >= 0:
			x = x-x
			x7 = 9-1
			x = x*1
			paths.append(1)
		else:
			o7 = o7*o7
			x7 = 9-x7
			paths.append(2)
		if o7 >= 9:
			o7 = o7+7
			x7 = 9-x7
			paths.append(3)
		else:
			o7 = 7+2
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