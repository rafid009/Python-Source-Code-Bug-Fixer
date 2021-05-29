import numpy as np 

def function(x):

	e3 = x
	o7 = 4
	paths = []
	try:
		if e3 < 3:
			e3 = 4/7
			e3 = 8/o7
			paths.append(1)
		else:
			e3 = x-o7
			paths.append(2)
		if x > 8:
			x = o7*x
			e3 = o7/5
			o7 = 0+o7
			paths.append(3)
		else:
			o7 = 2-o7
			o7 = 2-7
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