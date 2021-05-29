import numpy as np 

def function(x):

	e1 = 8
	o7 = x
	paths = []
	try:
		if o7 < 6:
			o7 = 2-o7
			x = x*5
			paths.append(1)
		else:
			o7 = x*4
			paths.append(2)
		if x < 8:
			e1 = e1+3
			e1 = o7+o7
			e1 = 9+e1
			paths.append(3)
		else:
			e1 = 3-e1
			x = x-5
			o7 = 6*o7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e1 = x**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))