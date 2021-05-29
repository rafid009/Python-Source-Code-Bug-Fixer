import numpy as np 

def function(x):

	o7 = 7
	e7 = x
	paths = []
	try:
		if e7 <= 2:
			o7 = e7-o7
			x = x+3
			o7 = o7*o7
			paths.append(1)
		else:
			o7 = 8/1
			e7 = e7-6
			paths.append(2)
		if o7 <= 7:
			e7 = e7-2
			paths.append(3)
		else:
			e7 = e7-e7
			x = x-9
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